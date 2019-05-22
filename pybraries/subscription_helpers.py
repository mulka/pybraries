# subscription_helpers.py
from requests.exceptions import HTTPError
import fire
from pybraries.helpers import sess, clear_params
from pybraries.make_request import make_request


def sub_api(action, *args, **kwargs):
    url_end_list = [
        "https://libraries.io/api/subscriptions"
    ]  # start of list to build url
    more_args = []  # for unpacking args
    url_combined = ""  # final string url
    call_type = ""  # post, put or delete
    manager = ""
    package = ""
    kind = "get"

    if kwargs:
        if "manager" in kwargs:
            manager = kwargs["manager"]
        if "package" in kwargs:
            package = kwargs["package"]

    if args:
        if args[0]:
            manager = args[0]
        if args[1]:
            package = args[1]

    if action == "list_subscribed":
        url_combined = "/".join(url_end_list)
        resp = make_request(url_combined, kind)
        return resp

    if action == "check_subscribed":
        # do we need to check for args?
        url_end_list.append(manager)
        url_end_list.append(package)
        url_combined = "/".join(url_end_list)
        print(url_combined)
        check = make_request(url_combined, kind)
        print(check)
        if check is not None:
            r_bool = True
        else:
            r_bool = False
            print(r_bool)
        return r_bool

    if action == "subscribe":
        kind = "post"
        url_end_list.append(manager)
        url_end_list.append(package)
        url_combined = "/".join(url_end_list)
        return make_request(url_combined, kind)

    if action == "update_subscribe":
        kind = "put"
        # not implemented - seems libraries.io api has bug
        # if implemented in future, adjust modules in readme

    if action == "delete_subscribe":
        kind = "delete"
        url_end_list.append(manager)
        url_end_list.append(package)
        url_combined = "/".join(url_end_list)
        return make_request(url_combined, kind)

    # first check if subscribed. Must be done before build url.
    # check_pkg_subscribed = Subscribe.check_subscribed(manager, package)
    # need to add back in

    # if call_type == "delete":  # and check_pkg_subscribed is None:
    #     msg = f"Unsubscribe unnecessary. You are not subscribed to {package}"
    #    return msg

    # pre = __check_prerelease(args, kwargs)
    """
    try:
        if r:
            if r.status_code == 204:
                response = f"Successfully unsubscribed from {package}"
            else:
                response = r.json()
            r.raise_for_status()
        return response
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:

        print(f"Other error occurred: {err}")
    """

    # currently has no effect when used (perhaps due to libraries.io api glitch)
    def __check_prerelease(*args, **kwargs):
        prerelease = kwargs.pop("include_prerelease", "")
        return prerelease