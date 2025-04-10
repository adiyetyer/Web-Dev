function checkAge(age) {
    return (age > 18) ? true : confirm('Did parents allow you?');
  }

  function checkAge(age) {
    return (age > 18) || confirm('Did parents allow you?');
  }

  
  function min(a, b) {
    return (a < b) ? a : b;
  } 

  function pow(x, n) {
    let result = 1;
    for (let i = 0; i < n; i++) {
      result *= x;
    }
    return result;
  } 

  function ask(question, yes, no) {
    if (confirm(question)) yes();
    else no();
  }
  
  ask(
    "Do you agree?",
  *!*
    () => alert("You agreed."),
    () => alert("You canceled the execution.")
  */!*
  );