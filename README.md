# Browser Logging Lambda
A simple lambda that will log any exceptions/requests sent to it, deploy with a Lambda URL and cloudwatch role https://docs.aws.amazon.com/lambda/latest/dg/lambda-urls.html.

In your browser javascript app, modify the window.onerror or add an event listener. Make a https call to the lambda to log the exception. This stack overflow has some examples: https://stackoverflow.com/questions/5328154/catch-all-javascript-errors-and-send-them-to-server

Here is a typescript example from a react application.
```
export const registerErrorHandlers = (): void => {
  window.addEventListener("error", (event: ErrorEvent): void => {
    postError(event.error);
  });

  const postError = (error: Error): void => {
    const xhr = new XMLHttpRequest();
    xhr.open("POST", ERROR_LOGGING_URL, true);
    xhr.send(
      JSON.stringify({
        name: error.name,
        message: error.message,
        stack: error.stack,
      })
    );
  };
};
```
