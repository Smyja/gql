import graphene
from graphene_django import DjangoObjectType
from djql.models import Restaurant, Quizzes, Category, Question, Answer


class RestaurantType(DjangoObjectType):
    class Meta:
        model = Restaurant
        fields = ("id", "name", "address")

class Query(graphene.ObjectType):
    restaurants = graphene.List(RestaurantType)

class RestaurantType(DjangoObjectType):
    class Meta:
        model = Restaurant
        fields = ("id", "name", "address")

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id","name")

class QuizzesType(DjangoObjectType):
    class Meta:
        model = Quizzes
        fields = ("id","title","category","quiz")

class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ("title","quiz")

class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ("question","answer_text")

class Query(graphene.ObjectType):
    restaurants = graphene.List(RestaurantType)
    all_questions = graphene.Field(QuestionType, id=graphene.Int())
    all_answers = graphene.List(AnswerType, id=graphene.Int())

    def resolve_all_questions(root, info, id):
        return Question.objects.get(pk=id)
    def resolve_all_answers(root, info, id):
        return Answer.objects.filter(question=id)
    def resolve_restaurants(self, info, **kwargs):
        return Restaurant.objects.all()

schema = graphene.Schema(query=Query)

    def resolve_restaurants(self, info, **kwargs):
        return Restaurant.objects.all()


schema = graphene.Schema(query=Query)
