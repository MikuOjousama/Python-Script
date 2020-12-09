import pycurl
import io
import sys

def run(url):
    b = io.BytesIO()
    c = pycurl.Curl()
    c.setopt(pycurl.TIMEOUT, 10)
    c.setopt(pycurl.CONNECTTIMEOUT, 10)
    c.setopt(pycurl.SSL_VERIFYPEER, 0)
    c.setopt(pycurl.SSL_VERIFYHOST, 0)
    c.setopt(pycurl.URL, url)
    c.setopt(pycurl.MAXREDIRS, 1)
    c.setopt(pycurl.WRITEFUNCTION, b.write)
    try:
        c.perform()
    except pycurl.error as e:
        print(e.args[1])
        sys.exit(e.args[0])
    print("URL: {}\n状态码: {}\n总消耗时间: {}\nDNS解析时间: {}\n建立连接消耗时间: {}\n下载内容长度: {}"
          .format(url, c.getinfo(pycurl.HTTP_CODE),
                    c.getinfo(pycurl.TOTAL_TIME),
                    c.getinfo(pycurl.NAMELOOKUP_TIME),
                    c.getinfo(pycurl.CONNECT_TIME),
                    int(c.getinfo(pycurl.SIZE_DOWNLOAD))
                 ))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: check  URL")
        sys.exit(1)
    run(sys.argv[1])


