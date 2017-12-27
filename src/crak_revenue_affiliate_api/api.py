import requests
from statics import urls, CONDITIONAL_FILTERS
import pdb

class CrackRevenueAffiliateAPI(object):

    def __init__(self, api_key):
        """
        """
        self.api_key = api_key
        self.session = requests.Session()
        pass

    def check_params(self, url, fields, **kwargs):
        """
        """
        for field in fields:
            if field not in urls[url]["params"]["required"]["fields[]"]["opts"]:
                raise Exception("FieldNotImplemented")
        #Kwargs include other optional parameters aside from fields
        for key, value in kwargs.items():
            if key not in urls[url]["params"]["optional"]:
                raise Exception("OptionNotImplemented")
            option = urls[url]["params"]["optional"][key]
            if "opts" in option:
                if "type" in option and not isinstance(value, option["type"]):
                    raise Exception("Wrong option type")
                if isinstance(value, dict):
                    for optkey, optvalue in value.items():
                        if optkey not in option["opts"]:
                            raise Exception("OptionNoSupported")
                if isinstance(value, list):
                    for val in value:
                        if val not in option["opts"]:
                            raise Exception("OptionNoSupported")
                        pass
                pass
            pass
        pass

    def build_fields():
        """"""
        pass

    def build_filters(self, filters):
        data = {}
        for f, v in filters.items():
            if CONDITIONAL_FILTERS[v[0]]["use"] == "flag":
                # Single tuple
                data["filters[{0}][conditional]".format(f)] = v[0]
                continue
            if CONDITIONAL_FILTERS[v[0]]["use"] == "value":
                data["filters[{0}][conditional]".format(f)] = v[0]
                data["filters[{0}][values]"] = v[1]
                continue
            if CONDITIONAL_FILTERS[f]["use"] == "range":
                data["filters[{0}][conditional]".format(f)] = v[0]
                data["filters[{0}][values][]"] = [v[1], v[2]]
                continue
        return data
        pass

    def build_sort(self, sorts):
        data ={}
        for k, v in sorts.items():
            data["sort[{0}]".format(k)] = v
        return data
        pass

    def get_affiliate_report(self, fields, **kwargs ):
        """
        """
        params = urls["Affiliate_Report"]["params"]["default"]
        params["api_key"] = self.api_key
        self.check_params("Affiliate_Report", fields=fields, **kwargs)
        params["fields[]"] = fields
        if "filters" in kwargs:
            params.update(self.build_filters(kwargs["filters"]))
        if "groups" in kwargs:
            params["groups[]"] = kwargs["groups"]
        if "sort" in kwargs:
            params.update(self.build_sort(kwargs["sort"]))
        self.affiliate_report_response = self.session.get(
            urls["Affiliate_Report"]["url"],
            params=params
        )
        return self.affiliate_report_response

    def get_affiliate_offer(self, fields, **kwargs):
        """
        """
        params = urls["Affiliate_Offer"]["params"]["default"]
        params["api_key"] = self.api_key
        self.check_params("Affiliate_Offer", fields=fields, **kwargs)
        params["fields[]"] = fields
        if "filters" in kwargs:
            params.update(self.build_filters(kwargs["filters"]))
        if "sort" in kwargs:
            params.update(self.build_sort(kwargs["sort"]))
        self.affiliate_report_response = self.session.get(
            urls["Affiliate_Offer"]["url"],
            params=params
        )
        return self.affiliate_report_response

    pass
