import os.path as op
import zipfile
import urllib.request


class nsd_downloader:
    """ Class to handle the download of files for nsd
    """

    def __init__(self, coco_annotation_path, coco_url='http://images.cocodataset.org/annotations/annotations_trainval2017.zip'):
        """ Downloader class

        Parameters
        ----------
        coco_annotation_path: str or Path
            Path to download the annotation file
        coco_url: str
            URL to downolad the annotation file
        """
        self.coco_annotation_path = coco_annotation_path
        self.coco_url = coco_url

    def download_coco_annotation_file(self):
        """ Downloads and extracts the relevant annotations files

        Parameters
        ----------
        url : str, optional
            url for zip file containing annotations.
            By default 'http://images.cocodataset.org/annotations/annotations_trainval2017.zip'
        """
        print(f"downloading annotations from {self.url}")
        filehandle, _ = urllib.request.urlretrieve(self.url)
        zip_file_object = zipfile.ZipFile(filehandle, 'r')
        zip_file_object.extractall(path=op.split(
            op.split(self.coco_annotation_path)[0])[0])
