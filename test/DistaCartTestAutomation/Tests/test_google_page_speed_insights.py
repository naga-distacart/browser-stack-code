# # -*- coding: utf-8 -*-
# import requests
# 
# GOOGLE_PAGE_SPEED_URL = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url="
# DISTA_API_KEY = "4795e6df8e5bd7bc9fd463bd35510fd2"
# DISTA_API_PWD = "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"
# API_HEADERS = {'X-Shopify-Api-Features': 'include-presentment-prices'}
# API_KEY = "AIzaSyDUmmAqTyiFQs9srW9Yrvq9orV0dkFssvE"
# DISTA_HOME_PAGE = "https://www.distacart.com/"
# DISTA_COLLECTION_PAGE = DISTA_HOME_PAGE + "collections/homeopathy-products"
# DISTA_PRODUCT_PAGE = DISTA_HOME_PAGE + "collections/baba-ramdev-patanjali-products/products/patanjali-giloy-ghan-vati-40-gm"
# cmd = ""
# collections_list = []
# products_list = []
# dista_page_speed = 0
# desktop_benchmark = {'overall_score': 90, 'fcp_score': 'FAST', 'fid_score': 'FAST', 'lcp_score': 'FAST',
#                      'cls_score': 'FAST','inp_score': 'FAST','ttfb_score': 'FAST'}
# mobile_benchmark = {'overall_score': 90, 'fcp_score': 'FAST', 'fid_score': 'FAST', 'lcp_score': 'FAST',
#                     'cls_score': 'FAST','inp_score': 'FAST','ttfb_score': 'FAST'}

#class TestGooglePageSpeedInsights:

    # def test_google_page_speed_insights_desktop(self, browser):
    #     #Speed Test for Home page
    #     global dista_page_speed, t
    #     t=0
    #     url = GOOGLE_PAGE_SPEED_URL + "https://www.distacart.com/products/isha-life-neem-and-turmeric-capsules" + "&strategy=desktop&locale=en&key=" + API_KEY
    #     while (True):
    #         response = requests.get(url)
    #         if (response.status_code == 200):
    #             break
    #     data = response.json()
    #     overall_score = data["lighthouseResult"]["categories"]["performance"]["score"] * 100
    #     try:
    #         assert overall_score > desktop_benchmark['overall_score']
    #     except:
    #         print("Overall Score is less than desktop benchmark")
    #         t=1
    #     fcp_score = data["loadingExperience"]["metrics"]["FIRST_CONTENTFUL_PAINT_MS"]["category"]
    #     try:
    #         assert fcp_score == desktop_benchmark['fcp_score']
    #     except:
    #         print("FCP Score is less than desktop benchmark")
    #         t=1
    #     fid_score = data["loadingExperience"]["metrics"]["FIRST_INPUT_DELAY_MS"]["category"]
    #     try:
    #         assert fid_score == desktop_benchmark['fid_score']
    #     except:
    #         print("FID Score is less than desktop benchmark")
    #         t=1
    #     lcp_score = data["loadingExperience"]["metrics"]["LARGEST_CONTENTFUL_PAINT_MS"]["category"]
    #     try:
    #         assert lcp_score == desktop_benchmark['lcp_score']
    #     except:
    #         print("LCP Score is less than desktop benchmark")
    #         t=1
    #     cls_score = data["loadingExperience"]["metrics"]["CUMULATIVE_LAYOUT_SHIFT_SCORE"]["category"]
    #     try:
    #         assert cls_score == desktop_benchmark['cls_score']
    #     except:
    #         print("CLS Score is less than desktop benchmark")
    #         t=1
    #     inp_score = data["loadingExperience"]["metrics"]["INTERACTION_TO_NEXT_PAINT"]["category"]
    #     try:
    #         assert inp_score == desktop_benchmark['inp_score']
    #     except:
    #         print("INP Score is less than desktop benchmark")
    #         t=1
    #     ttfb_score = data["loadingExperience"]["metrics"]["EXPERIMENTAL_TIME_TO_FIRST_BYTE"]["category"]
    #     try:
    #         assert ttfb_score == desktop_benchmark['ttfb_score']
    #     except:
    #         print("TTFB Score is less than desktop benchmark")
    #         t=1
    #     assert t == 0
    # 
    # def test_google_page_speed_insights_mobile(self, browser):
    #     #Home page -Mobile
    #     url = GOOGLE_PAGE_SPEED_URL + "https://www.distacart.com/products/isha-life-neem-and-turmeric-capsules" + "&strategy=mobile&locale=en&key=" + API_KEY
    #     while (True):
    #         response = requests.get(url)
    #         if (response.status_code == 200):
    #             break
    #     data = response.json()
    #     overall_score_mobile = data["lighthouseResult"]["categories"]["performance"]["score"] * 100
    #     try:
    #         assert overall_score_mobile == desktop_benchmark['overall_score_mobile']
    #     except:
    #         print("Overall Score is less than mobilebenchmark")
    #         t=1
    #     fcp_score_mobile = data["loadingExperience"]["metrics"]["FIRST_CONTENTFUL_PAINT_MS"]["category"]
    #     try:
    #         assert fcp_score_mobile == desktop_benchmark['fcp_score_mobile']
    #     except:
    #         print("FCP Score is less than mobile benchmark")
    #         t=1
    #     fid_score_mobile = data["originLoadingExperience"]["metrics"]["FIRST_INPUT_DELAY_MS"]["category"]
    #     try:
    #         assert fid_score_mobile == desktop_benchmark['fid_score_mobile']
    #     except:
    #         print("FID Score is less than the mobile benchmark")
    #         t=1
    #     lcp_score_mobile = data["originLoadingExperience"]["metrics"]["LARGEST_CONTENTFUL_PAINT_MS"]["category"]
    #     try:
    #         assert lcp_score_mobile == desktop_benchmark['lcp_score_mobile']
    #     except:
    #         print("LCP Score is lesss than the mobile benchmanrk")
    #         t=1
    #     cls_score_mobile = data["originLoadingExperience"]["metrics"]["CUMULATIVE_LAYOUT_SHIFT_SCORE"]["category"]
    #     try:
    #         assert cls_score_mobile == desktop_benchmark['cls_score_mobile']
    #     except:
    #         print("CLS Score is less than mobile benchmark")
    #         t=1
    #     inp_score_mobile = data["originLoadingExperience"]["metrics"]["INTERACTION_TO_NEXT_PAINT"]["category"]
    #     try:
    #         assert inp_score_mobile == desktop_benchmark['inp_score_mobile']
    #     except:
    #         print("INP Score is less than the mobile benchmark")
    #         t=1
    #     ttfb_score_mobile = data["originLoadingExperience"]["metrics"]["EXPERIMENTAL_TIME_TO_FIRST_BYTE"]["category"]
    #     try:
    #         assert ttfb_score_mobile == desktop_benchmark['ttfb_score_mobile']
    #     except:
    #         print("TTFB Score is less than the mobile benchmark")
    #         t=1
    #     assert t==0

