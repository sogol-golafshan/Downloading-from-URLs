import requests
import pandas as pd
import rectanglecropper.crop as rc
import os


def download_image():
    dataset = pd.read_csv('YourFranchiseAdvisors-20210927.csv')
    urlcol = dataset.iloc[:, 1].values

    for url in urlcol:
        filename = url.split('/')[-1]
        r = requests.get(url, allow_redirects=True)
        try:
            os.makedirs('./images')
        except OSError:
            pass

        open(os.path.join('./images',filename) , 'wb').write(r.content)


def crop_image():
    main_path = './images'
    path = os.listdir(main_path)
    print(path)
    try:
        os.makedirs('./rectangle_images')
    except OSError:
        pass
    for root, dirs, files in os.walk("./images"):
        for p in files:
            print(os.path.join(main_path, p))
            cropper = rc.RectangleImageCrop()
            cropper.open(image_path=os.path.join(main_path, p))
            cropper.crop(min_crop_width=50)
            cropper.save(saved_path='./rectangle_images', filename=p + '_rect', saved_format='jpeg')


def compress_images():
    try:
        os.makedirs('./compressed_images')
    except OSError:
        pass
    os.system('pip3 install git+https://github.com/thaiminhpv/batch-jpeg-compressor@main ; '
              'batch_jpeg_compressor images compressed_images')


def rename():
    path = './compressed_images'
    for root, dirs, files in os.walk(path):
        print(files)
        for file in files:
            root, ext = os.path.splitext(file)
            print("-logo".join([root, ext]))


def main():
    download_image()
    # crop_image()
    compress_images()
    rename()


if __name__ == '__main__':
    main()