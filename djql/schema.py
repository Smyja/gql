import graphene
from graphene_django import DjangoObjectType
from djql.models import Restaurant, Quizzes, Category, Question, Answer


class RestaurantType(DjangoObjectType):
    class Meta:
        model = Restaurant
        fields = ("id", "name", "address")


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name")


class QuizzesType(DjangoObjectType):
    class Meta:
        model = Quizzes
        fields = ("id", "title", "category")


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ("title", "quiz")


class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ("question", "answer_text")


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


class CategoryMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String(required=True)

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, name,id):
        category= Category.objects.get(id=id)
        category.name= name
        category.save()
        return CategoryMutation(category=category)


#create a new quiz

class CategoryCreate(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, name):
        category = Category(name=name)
        category.save()
        return CategoryCreate(category=category)
class QuizzesMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        title = graphene.String(required=True)
        category = graphene.String(required=True)

    quizzes = graphene.Field(QuizzesType)

    @classmethod
    def mutate(cls, root, info, title, category, id):
        quizzes = Quizzes.objects.get(id=id)
        quizzes.title = title
        quizzes.category = category
        quizzes.save()
        return QuizzesMutation(quizzes=quizzes)
class Mutation(graphene.ObjectType):
    update_category = CategoryMutation.Field()
    update_quizzes = QuizzesMutation.Field()
    create_category = CategoryCreate.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
