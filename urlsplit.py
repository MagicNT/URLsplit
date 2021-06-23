import prettytable
from urllib.parse import unquote, urlparse
from argparse import ArgumentParser


################################################################################

    
def get_value(component):
    if component:
        return component
    else:
        return ""


def split(url_string):
    print("\n [+] URL: {}\n".format(unquote(url_string)))
    url = urlparse(url_string)

    t = prettytable.PrettyTable(["Component", "Value"])
    t.add_row(["Scheme", get_value(url.scheme)])
    t.add_row(["Username", get_value(url.username)])
    t.add_row(["Password", get_value(url.password)])
    t.add_row(["Host", get_value(url.hostname)])
    t.add_row(["Port", get_value(url.port)])
    t.add_row(["Path", get_value(url.path)])
    print(t)
    print("")


    param = url.query
    if param:
        t = prettytable.PrettyTable(["Parameter", "Value"])
        
        if "&" not in param:
            param += "&"
        param = param.split("&")

        for p in list(filter(None, param)):
            try:
                attribute, value = p.split("=")
            except:
                attribute = p
                value = ""
            t.add_row([attribute, value])

        print(t)
        print("")


    fragm = url.fragment
    if fragm:
        t = prettytable.PrettyTable(["Fragment", "Value"])

        if "&" in fragm:
            fragm = fragm.split("&")
        elif ";" in fragm:
            fragm = fragm.split(";")
        else:
            fragm += "&"
            fragm = fragm.split("&")

        for p in list(filter(None, fragm)):
            try:
                attribute, value = p.split("=")
            except:
                attribute = p
                value = ""
            t.add_row([attribute, value])

        print(t)
        print("")


################################################################################


def main():
    f = ArgumentParser()
    f.add_argument("-u", "--url", help="The URL to parse.")
    ARG = f.parse_args()
    
    split(ARG.url)


################################################################################


if __name__ == '__main__':
    main()


################################################################################

