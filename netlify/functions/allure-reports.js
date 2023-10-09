exports.handler = async (event, context) => {
  try {
    // Ваша функція для виконання HTTP-запиту до GitHub API
    const allureData = await fetchDataFromGitHub();

    // Тут ви можете обробити дані звітів Allure і підготувати їх для відображення на сайті

    return {
      statusCode: 200,
      body: JSON.stringify(allureData),
    };
  } catch (error) {
    return {
      statusCode: 500,
      body: JSON.stringify({ error: 'Something went wrong' }),
    };
  }
};
