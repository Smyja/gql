# gql

To run a Query.
```graphql
query GetQuestions {
  allQuestions(id:1){
    title
  }
  allAnswers(id:1){
    answerText
  }
  
}
```

To run a mutation 
```graphql
mutation addcate{
  updateCategory(id:1,name:"jops"){
    category{
      name
    }
  }
}
```