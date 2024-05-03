from django.utils.text import slugify
import string
import random


# Slug generator için random string oluşturulmasını sağlıyor
def generate_random_string(N):
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = N))
    return res

# Slug generator. Django'ya özgü Slug oluşturulmasını sağlıyor
def generate_slug(text):
    new_slug = slugify(text)
    from home.models import BlogModel
    if BlogModel.objects.filter(slug = new_slug).first():
        return generate_slug(text + generate_random_string(5))
    return new_slug