# Downloading-from-URLs

a python script that takes an image from a URL and does the following:

    downloads the image

    crops it to the borders of the logo (removing padding)

    compresses it

    re-names it to be [franchiseName]-logo

    uploads the optimized file to Wasabi account

    gets the new URL from Wasabi and updates the pg database
