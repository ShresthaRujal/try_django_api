from rest_framework import serializers
from rest.models import User,Post,Comment
# we need to provide way of SE and DE the model instances into representations such as jsonself.

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields='__all__'

    def create(self,user_objs):
        # Creates a new object, saves it and puts it in the related object set. Returns the newly created object.
        return User.objects.create(**user_objs)

    def update(self,instance,user_objs):
        instance.name=user_objs.get('name',instance.name)
        instance.email=user_objs.get('email',instance.email)
        instance.password=user_objs.get('password',instance.password)
        instance.created_date=user_objs.get('created_date',instance.created_date)
        instance.address=user_objs.get('address',instance.address)
        instance.save()
        return instance


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields='__all__'

    def create(self,post_objs):
        # Creates a new object, saves it and puts it in the related object set. Returns the newly created object.
        return Post.objects.create(**post_objs)

    def update(self,instance,post_objs):
        instance.author = post_objs.get('author',instance.author)
        instance.title = post_objs.get('title',instance.title)
        instnace.text = post_objs.get('text',instance.text)
        instance.create_date = post_objs.get('create_date',instance.create_date)
        instance.published_date = post_objs.get('published_date',instance.published_date)
        instance.save()
        return instance

    def publish(self):
        self.published_date=timezone.now()
        self.save()


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields='__all__'

    def create(self,comment_objs):
        # Creates a new object, saves it and puts it in the related object set. Returns the newly created object.
        return Comment.objects.create(**comment_objs)

    def update(self,instance,comment_objs):
        instance.post = comment_objs.get('post',instance.post)
        instance.author = comment_objs.get('author',instance.author)
        instance.text = comment_objs.get('text',instance.text)
        instance.create_date = comment_objs.get('create_date',instance.create_date)
        instance.approved_comment = comment_objs.get('approved_comment',instance.approved_comment)
        instance.save()
        return instance

    def setPost(self, post):
        self.post = post

    def approve(self):
        self.approved_comment=True
        self.save()
