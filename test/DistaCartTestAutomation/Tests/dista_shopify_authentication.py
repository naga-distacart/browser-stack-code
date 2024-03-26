'''
Authentication for shopify backend
'''

class DistaShopifyAuthentication():
    '''Parameters to authentication to shopify backend'''
    _shopify_timestamp_format = '%Y-%m-%dT%H:%M:%S'
    _api_password             = ''
    _store_name               = 'browntaped'
    _api_version              = '2023-01'
    _shopify_timestamp_format = '%Y-%m-%dT%H:%M:%S'
    _dista_shop_url           = "https://%s.myshopify.com/admin/api/%s" % (_store_name, _api_version)

    def __init__(self, **kwargs):
        if ('objects_per_query' in kwargs):
            self._objects_per_query     = kwargs['objects_per_query']
        else:
            self._objects_per_query     = 250

    def dista_shopify_access_token_get(self):
        if (self._api_password):
            return self._api_password
        else:
            return self.__class__._api_password

    def dista_shopify_objects_per_query_get(self):
        return self._objects_per_query

    @classmethod
    def dista_shopify_url_get(cls):
        return cls._dista_shop_url

    def dista_shopify_timestamp_format_get(cls):
        return cls._shopify_timestamp_format

def main():
    pass

if __name__ == "__main__":
    main()
