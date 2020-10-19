import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from App.configs.defs import headers, files_downloaded


class ExtractCssJsFiles:
    def __init__(self, url):
        self.url = url

    def extractfiles(self):
        #url = 'https://www.w3.org/TR/css-fonts-4/'
        session = requests.Session()
        session.headers["User-Agent"] = headers
        html = session.get(self.url).content
        soup = BeautifulSoup(html, 'html.parser')

        # get the JavaScript files
        script_files = []

        for script in soup.find_all("script"):
            if script.attrs.get("src"):
                # if the tag has the attribute 'src'
                script_url = urljoin(self.url, script.attrs.get("src"))
                script_files.append(script_url)

        # get the CSS files
        css_files = []

        for css in soup.find_all("link"):
            if css.attrs.get("href"):
                # if the link tag has the 'href' attribute
                css_url = urljoin(self.url, css.attrs.get("href"))
                css_files.append(css_url)

        print("Total JavaScript files in the page:", len(script_files))
        print("Total CSS files in the page:", len(css_files))

        # write file links into files
        with open(files_downloaded + "javascript_files.txt", "w") as f:
            for js_file in script_files:
                print(js_file, file=f)

        with open(files_downloaded + "css_files.txt", "w") as f:
            for css_file in css_files:
                print(css_file, file=f)

extract_def = ExtractCssJsFiles("https://www.w3.org/TR/css-fonts-4/")



