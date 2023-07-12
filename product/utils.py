import os


def get_upload_path(instance, filename):
    filename, ext = os.path.splitext(filename)
    return os.path.join(instance.__class__.__name__.lower() + "_images", f"{instance.slug}{ext}")