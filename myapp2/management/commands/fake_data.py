import random
from django.core.management.base import BaseCommand

from ...models import Product, User, Category

# category = ['phone', 'tv', 'big_technic', 'accessory']
category = Category.objects.all()
class Command(BaseCommand):
    help = "Generate fake authors and posts."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        # for i in range(1, count + 1):
        #     author = User(name=f'Name{i}', email=f'mail{i}@mail.ru', t_number=f'700-{i}34-{i+1}4{i}',
        #                   adress=f'Ivanova{i+3},ap{i}8{random.randrange(0, 10)}')
        #     author.save()
        for j in range(1, count + 1):

            tmp1 = random.choice(category)
            print(tmp1)
            post = Product(name=f'{tmp1}Name{j*random.randrange(0, 10)}', category=tmp1,
                           description=f'discription: {tmp1} #{j*random.randrange(0, 10)} is bla bla bla many long text',
                        price=random.randint(10,20)*j, quantity=random.randint(1,20))
            post.save()
