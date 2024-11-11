def generate_prompt(question: str, contexts: list):
  # character limit for the prompt
  limit = 3000


  # build our prompt with the retrieved contexts included
  prompt_start = (
      "Answer the question based on the context below.\n\n"+
      "Context:\n"
  )
  prompt_end = (
      f"\n\nQuestion: {question}\nAnswer:"
  )

  # append contexts until hitting limit
  for i in range(1, len(contexts)):
      if len("\n\n---\n\n".join(contexts[:i])) >= limit:
          prompt = (
              prompt_start +
              "\n\n---\n\n".join(contexts[:i-1]) +
              prompt_end
          )
          break
      elif i == len(contexts)-1:
          prompt = (
              prompt_start +
              "\n\n---\n\n".join(contexts) +
              prompt_end
          )
  return prompt


