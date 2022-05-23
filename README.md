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