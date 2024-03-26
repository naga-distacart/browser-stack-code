'''
Utility APIs to access shopify backend database
'''

import requests, time, pytz, re
from datetime import datetime
from DistaCartTestAutomation.Tests.dista_shopify_authentication import DistaShopifyAuthentication
from DistaCartTestAutomation.Tests.dista_constants import *
from DistaCartTestAutomation.Tests.dista_misc import is_dst



class ShopifyAPIClass():
    '''Methods to interact with shopify API classes

    Supported API classes:
    1. products
    2. variants
    3. shop
    '''
    def __init__(self, api_class, **kwargs):
        self._api_class       = api_class
        self._timestamp_keys  = {'created_at_min', 'created_at_max', 'updated_at_min', 'updated_at_max'}
        self._dista_params = DistaShopifyAuthentication()

    def _shopify_access_token_get(self):
        return self._dista_params.dista_shopify_access_token_get()

    def _shopify_use_next_access_token(self):
        pass

    def shopify_object_metafield_get(self, object_id = None, filters = {}):
        """Method to get metafields for a given object belonging to shopify_api_class_get().

        Arguments:
            1. object_id : type: unsigned integer, mandatory.
            2. filters   : type: dictionary, optional.
                Keys for filters:
                    1. key       : Name of key, type: string, optional.
                    2. namespace : Namespace, type: string, optional.
                E.g.
                    filters['key']       = "inventory"
                    filters['namespace'] = "distacart"

        Return: List of metafields that match the filters.
        """
        shopify_metafield_list = []
        filter_string = self._shopify_filter_string_get(filters)

        if (self._api_class != 'shop'):
            response = self.shopify_objects_rest_get("%s/%s/metafields.json?%slimit=%s" % (self._api_class, object_id, filter_string, self._dista_params.dista_shopify_objects_per_query_get()))
        else:
            response = self.shopify_objects_rest_get("/metafields.json?%slimit=%s" % (filter_string, self._dista_params.dista_shopify_objects_per_query_get()))
        if (not response):
            return shopify_metafield_list

        shopify_metafield_list = response.json()['metafields']

        while ('next' in response.links):
            next_url = response.links['next']['url']
            next_page_info = re.search('page_info.*', next_url)
            cookie = re.search('=.*', next_page_info.group(0)).group(0)[1:]
            response = self.shopify_objects_rest_get("%s/%s/metafields.json?limit=%s&page_info=%s" % (self._api_class, object_id, self._dista_params.dista_shopify_objects_per_query_get(), cookie))
            if (response):
                shopify_metafield_list.extend(response.json()['metafields'])
        return shopify_metafield_list

    def shopify_objects_rest_get(self, request_string, **kw_args):
        headers = {'X-Shopify-Access-Token': self._shopify_access_token_get()}
        if ('headers' in kw_args):
            headers = {headers, kw_args['headers']}
        request_string = "%s/%s" % (DistaShopifyAuthentication.dista_shopify_url_get(), request_string)
        while True:
            while True:
                sleep_time = 1
                try:
                    response = requests.get(request_string, headers=headers)
                    break
                except:
                    time.sleep(sleep_time)
                    sleep_time += 1
            if (response.status_code == REST_SUCCESS): break
            if (response.status_code == REST_NOT_FOUND):
                return
            if (response.status_code == REST_UNAUTHORIZED):
                raise PermissionError("Unauthorized access")
            if (response.status_code == REST_TOO_MANY_REQUESTS):
                self._shopify_use_next_access_token()
                headers['X-Shopify-Access-Token'] = self._shopify_access_token_get()
                time.sleep(int(float(response.headers['Retry-After'])))
        return response

    def _shopify_timestamp_get(self, timestamp):
        if ('year' not in timestamp):
            raise KeyError("'year' not passed!")
        if ('month' not in timestamp):
            raise KeyError("'month' not passed!")
        if ('day' not in timestamp):
            raise KeyError("'day' not passed!")
        if ('hour' not in timestamp):
            timestamp['hour'] = 0
        if ('minute' not in timestamp):
            timestamp['minute'] = 0
        if ('second' not in timestamp):
            timestamp['second'] = 0
        x = datetime(year = timestamp['year'], month = timestamp['month'], day = timestamp['day'], hour = timestamp['hour'], minute = timestamp['minute'], second = timestamp['second'],  tzinfo=pytz.timezone('US/Pacific'))
        dst = is_dst(datetime(timestamp['year'], timestamp['month'], timestamp['day'], timestamp['hour']), timezone="US/Pacific")
        if (dst):
            offset = "-07:00"
        else:
            offset = "-08:00"
        return x.strftime(self._dista_params.dista_shopify_timestamp_format_get()) + offset

    def _shopify_filter_string_get(self, filters):
        """Method to generate the filter string for the rest query"""
        filter_string = ''
        for k, v in filters.items():
            val = v
            if (k in self._timestamp_keys):
                val = self._shopify_timestamp_get(v)
            filter_string += '%s=%s&' % (k, val)
        return filter_string

def main():
    variants = ShopifyAPIClass('variants')
    shop = ShopifyAPIClass('shop')
    mf = variants.shopify_object_metafield_get(13750313549869, filters={'key' : 'rapid_delivery', 'namespace' : "distacart"})
    print(mf[0]['value'])
    # mf1=variants.shopify_object_metafield_get(42164399276191, filters={'key' : 'product_ready_to_ship_t', 'namespace' : "distacart"})

    # print(mf1)

if __name__ == "__main__":
    main()
