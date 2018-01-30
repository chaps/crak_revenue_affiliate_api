import requests
from .statics import urls, CONDITIONAL_FILTERS


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
            if field not in urls[url][
                        "params"]["required"]["fields[]"]["opts"]:
                raise Exception("{0} FieldNotImplemented".format(field))
        # Kwargs include other optional parameters aside from fields
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
                            raise Exception(
                                "{0} OptionNoSupported \
                                supported options are: {1}".format(
                                    optkey, option["opts"].keys()
                                )
                            )
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
            if not isinstance(v, type([])) and not isinstance(v, type((0,))):
                raise Exception(
                    "\"{0}\" is not of type list or tuple".format(str(v))
                )
            if len(v) == 0:
                raise Exception("{0} received empty list or tuple".format(f))
                pass
            if v[0] not in CONDITIONAL_FILTERS:
                raise Exception(
                    "'{0}' not in CONDITIONAL_FILTERS options are {1}".format(
                        v[0], CONDITIONAL_FILTERS.keys()
                    )
                )

            if CONDITIONAL_FILTERS[v[0]]["use"] == "flag":
                # Single tuple
                data["filters[{0}][conditional]".format(f)] = v[0]
                continue
            if CONDITIONAL_FILTERS[v[0]]["use"] == "value":
                # 2 Values, Conditional and value
                data["filters[{0}][conditional]".format(f)] = v[0]
                if len(v) != 2:
                    raise Exception(
                        "{0}:{1} must receive 2 values \
                        Conditional and value".format(f, v)
                    )
                data["filters[{0}][values]".format(f)] = v[1]
                continue
            if CONDITIONAL_FILTERS[f]["use"] == "range":
                # 3 Values, Conditional, Lower Bound value, Upper bound value.
                if len(v) == 0:
                    raise Exception(
                        "{0} received empty list or tuple".format(f)
                    )
                data["filters[{0}][conditional]".format(f)] = v[0]
                data["filters[{0}][values][]"] = [v[1], v[2]]
                continue
        return data
        pass

    def build_sort(self, sorts):
        data = {}
        for k, v in sorts.items():
            data["sort[{0}]".format(k)] = v
        return data

    def get_affiliate_report(self, fields, **kwargs):
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
