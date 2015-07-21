import os
import textract

from collections import defaultdict

from skeeter import exception

class CmdLineRunner(object):
    """Command Line Runner"""

    IGNORE_FILES = ['contributors.md', 'README.md']

    def __init__(self, path, verbose=False, types=None):

        if not os.path.isdir(path):
            raise exception.TargetPathError("Target path is not a directory")

        if not os.access(path, os.R_OK):
            raise exception.BadPermissions("Target path is not readable")

        self.path = path
        self.types = ['all'] if types is None else types
        self.verbose = verbose

    def list_files(self, path):
        filelist = set()

        for root, dirs, files in os.walk(path):
            for filename in files:
            	abs_path = os.path.join(root, filename)

                if ".git" in abs_path or filename in self.IGNORE_FILES:
                    continue

                if ".pdf.1" in filename:
                    filename = filename.replace(".pdf.1",".pdf")

                if ".md" in filename:
                    filename = filename.replace(".md",".txt")

                filelist.add(abs_path)

        return filelist

    def quick_quotes(self, fileName):
        try:
            txt = textract.process(fileName)
        except Exception as e:
            pass # mmm :(
        finally:
            return txt

    def extract_ioc(self, text):
        IOCs = []
        lines = text.split("\n")

        for line in lines:
            if "MD5"in self.types:
                temp = []
                for m in re.finditer(reMD5, line, re.IGNORECASE):
                    temp.append(m.group())
                    for item in temp:
                        if checkers.checkmd5(item):
                            IOCs.append(item)

            if "IPv4" in self.types:
                temp=[]
            for n in re.finditer(reIPv4, line, re.IGNORECASE):
                    temp.append(n.group())
                    for item in temp:
                        item=item.translate(None, "[]")
                        if checkers.checkip(item):
                            IOCs.append(item)

            if "URL" in self.types:
                temp=[]
            for o in re.finditer(reURL, line, re.IGNORECASE):
                    temp.append(o.group())
                    for item in temp:
                        item=item.translate(None, "[]")
                        item=item.replace("http://", "")
                        item=item.replace("https://", "")
                        if checkers.checkurl(item):
                            IOCs.append(item)

            if "Domain" in self.types:
                temp=[]
            for p in re.finditer(reDomain, line, re.IGNORECASE):
                    temp.append(p.group())
                    for item in temp:
                        item=item.lower()
                        item=item.translate(None, "[]")
                        if checkers.checkdomain(item):
                            IOCs.append(item)

            if "Email" in self.types:
            temp=[]
                for q in re.finditer(reEmail, line, re.IGNORECASE):
                    temp.append(q.group())
                    for item in temp:
                        item=item.lower()
                        item=item.translate(None, "[]")
                        if checkers.checkemailadd(item):
                            IOCs.append(item)

        return IOCs

    def run(self):
        """Run scrapping"""

        iocs = defaultdict(set)
        for filepath in list_files(self.path):
            text = quick_quotes(filepath)
            indicators = indicators + extractIOC(text,["Domain", "MD5", "IPv4", "URL", "Email"])
		
