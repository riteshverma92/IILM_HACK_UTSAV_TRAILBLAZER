// let btnlog = document.querySelector(".login-btn");
// let blkscn = document.querySelector(".overlay");
// let btnsign =document.querySelector(".signup-btn");
// let nxtbtn = document.querySelector(".next");
// let sdOTPbtn =document.querySelector(".sendotp");
// import { window } from "window"; 



document.addEventListener("DOMContentLoaded", function() {
  if (document.querySelector(".login-btn")) {
    // Code specific to the login page
    let btnlog = document.querySelector(".login-btn");
    let blkscn = document.querySelector(".overlay");
    let btnsign = document.querySelector(".signup-btn");

    btnlog.addEventListener("click", showloginform);
    blkscn.addEventListener("click", closeform);
    btnsign.addEventListener("click", showsignupform);

    function closeform() {
      // Your code here...
      document.querySelector(".overlay").classList.remove("overlay-nt");
      document.querySelector(".login-form").classList.remove("login-form-after-click");
      document.querySelector(".signup-form").classList.remove("signup-form-after-click");
      document.querySelector(".signup-form-nxt").classList.remove(".signup-form-after-click");
    }

    function showloginform() {
      // Your code here...
      document.querySelector(".overlay").classList.add("overlay-nt");
      document.querySelector(".login-form").classList.add("login-form-after-click");
    }

    function showsignupform() {
      // Your code here...
      document.querySelector(".overlay").classList.add("overlay-nt");
      document.querySelector(".signup-form").classList.add("signup-form-after-click");
    }
  }

  // if (document.querySelector("#quiz")) {
  //   // Code specific to the quiz page
  //   const quizData = [
  //     // Your quiz data here...
  //   ];

  //   const quizContainer = document.getElementById('quiz');
  //   const resultContainer = document.getElementById('result');
  //   const submitButton = document.getElementById('submit');

  //   // Your quiz functions here...
  // }

  if (document.querySelector("#a")) {
    // Code specific to the courses page
    let btn_a = document.querySelector("#a");
    let cancel1 = document.querySelector("#cross-a");
    // let btn_a = document.querySelector("#a");
let btn_b = document.querySelector("#b");
let btn_c = document.querySelector("#c");
let btn_d = document.querySelector("#d");
// let cancel1 = document.querySelector("#cross-a");
let cancel2 =  document.querySelector("#cross-b");
let cancel3 = document.querySelector("#cross-c");
let cancel4 =  document.querySelector("#cross-d");

    btn_a.addEventListener("click", () => {
      // Your code here...
      document.querySelector(".overlay").classList.add("overlay-nt");
      document.querySelector(".popup_a").classList.add("popup_a-after");
    });
    cancel1.addEventListener("click", () => {
      // Your code here...
      document.querySelector(".overlay").classList.remove("overlay-nt");
      document.querySelector(".popup_a").classList.remove("popup_a-after");
    });
    btn_b.addEventListener("click", () => {
      // Your code here...
      document.querySelector(".overlay").classList.add("overlay-nt");
      document.querySelector(".popup_b").classList.add("popup_b-after");
    });
    cancel2.addEventListener("click", () => {
      // Your code here...
      document.querySelector(".overlay").classList.remove("overlay-nt");
      document.querySelector(".popup_b").classList.remove("popup_b-after");
    });
    btn_c.addEventListener("click", () => {
      // Your code here...
      document.querySelector(".overlay").classList.add("overlay-nt");
      document.querySelector(".popup_c").classList.add("popup_c-after");
    });
    cancel3.addEventListener("click", () => {
      // Your code here...
      document.querySelector(".overlay").classList.remove("overlay-nt");
      document.querySelector(".popup_c").classList.remove("popup_c-after");
    });
    btn_d.addEventListener("click", () => {
      // Your code here...
      document.querySelector(".overlay").classList.add("overlay-nt");
      document.querySelector(".popup_d").classList.add("popup_d-after");
    });
    cancel4.addEventListener("click", () => {
      // Your code here...
      document.querySelector(".overlay").classList.remove("overlay-nt");
      document.querySelector(".popup_d").classList.remove("popup_d-after");
    });

    // Similar code for btn_b, btn_c, etc...
  }
});


// window.onclick = function(event) {
//   if (!event.target.matches('.dropbtn')) {
//       var dropdowns = document.getElementsByClassName("dropdown-content");
//       for (var i = 0; i < dropdowns.length; i++) {
//           var openDropdown = dropdowns[i];
//           if (openDropdown.classList.contains('show')) {
//               openDropdown.classList.remove('show');
//           }
//       }
//   }
// };



// btnlog.addEventListener("click", showloginform);
// blkscn.addEventListener("click", closeform);
// btnsign.addEventListener("click", showsignupform);
// // nxtbtn.addEventListener("click", shownextsignup);       removed this btn!

// // sdOTPbtn.addEventListener("click", () => {
// //     document.querySelector(".otp-popup").classList.add("otp-popup-hide");
// //     document.querySelector(".signup-form").classList.remove("signup-form-after-click")
// // });


// function closeform(){
//     document.querySelector(".overlay").classList.remove("overlay-nt");
//     document.querySelector(".login-form").classList.remove("login-form-after-click");
//     document.querySelector(".signup-form").classList.remove("signup-form-after-click");
//     document.querySelector(".signup-form-nxt").classList.remove(".signup-form-after-click");
// }

// function showloginform(){
//     document.querySelector(".overlay").classList.add("overlay-nt");
//     document.querySelector(".login-form").classList.add("login-form-after-click");
// }

//  function showsignupform(){
//      document.querySelector(".overlay").classList.add("overlay-nt");
//     document.querySelector(".signup-form").classList.add("signup-form-after-click");
// }

// function shownextsignup(){ //signup (not in use right now)
//     // document.querySelector(".signup-form").classList.remove(".first-page-signup-page");
//     document.querySelector(".first-page-signup-page").classList.add("first-page-aftr-clik");
//     // document.querySelector(".signup-form").classList.add(".sec-page-signup-form");
//     document.querySelector(".sec-page-signup-form").classList.add("signup-form-nxt-ka-nxt");
// }

// quiz-js------------------------------------------------------------------------------------------------------------------------------------------

// const quizData = [
//     {
//       question: 'What is the capital of France?',
//       options: ['Paris', 'London', 'Berlin', 'Madrid'],
//       answer: 'Paris',
//     },
//     {
//       question: 'What is the largest planet in our solar system?',
//       options: ['Mars', 'Saturn', 'Jupiter', 'Neptune'],
//       answer: 'Jupiter',
//     },
//     {
//       question: 'Which country won the FIFA World Cup in 2018?',
//       options: ['Brazil', 'Germany', 'France', 'Argentina'],
//       answer: 'France',
//     },
//     {
//       question: 'What is the tallest mountain in the world?',
//       options: ['Mount Everest', 'K2', 'Kangchenjunga', 'Makalu'],
//       answer: 'Mount Everest',
//     },
//     {
//       question: 'Which is the largest ocean on Earth?',
//       options: [
//         'Pacific Ocean',
//         'Indian Ocean',
//         'Atlantic Ocean',
//         'Arctic Ocean',
//       ],
//       answer: 'Pacific Ocean',
//     },
//     {
//       question: 'What is the chemical symbol for gold?',
//       options: ['Au', 'Ag', 'Cu', 'Fe'],
//       answer: 'Au',
//     },
//     {
//       question: 'Who painted the Mona Lisa?',
//       options: [
//         'Pablo Picasso',
//         'Vincent van Gogh',
//         'Leonardo da Vinci',
//         'Michelangelo',
//       ],
//       answer: 'Leonardo da Vinci',
//     },
//     {
//       question: 'Which planet is known as the Red Planet?',
//       options: ['Mars', 'Venus', 'Mercury', 'Uranus'],
//       answer: 'Mars',
//     },
//     {
//       question: 'What is the largest species of shark?',
//       options: [
//         'Great White Shark',
//         'Whale Shark',
//         'Tiger Shark',
//         'Hammerhead Shark',
//       ],
//       answer: 'Whale Shark',
//     },
//     {
//       question: 'Which animal is known as the King of the Jungle?',
//       options: ['Lion', 'Tiger', 'Elephant', 'Giraffe'],
//       answer: 'Lion',
//     },
//   ];
  
//   const quizContainer = document.getElementById('quiz');
//   const resultContainer = document.getElementById('result');
//   const submitButton = document.getElementById('submit');
//   const retryButton = document.getElementById('retry');
//   const showAnswerButton = document.getElementById('showAnswer');
  
//   let currentQuestion = 0;
//   let score = 0;
//   let incorrectAnswers = [];
  
//   function shuffleArray(array) {
//     for (let i = array.length - 1; i > 0; i--) {
//       const j = Math.floor(Math.random() * (i + 1));
//       [array[i], array[j]] = [array[j], array[i]];
//     }
//   }
  
//   function displayQuestion() {
//     const questionData = quizData[currentQuestion];
  
//     const questionElement = document.createElement('div');
//     questionElement.className = 'question';
//     questionElement.innerHTML = questionData.question;
  
//     const optionsElement = document.createElement('div');
//     optionsElement.className = 'options';
  
//     const shuffledOptions = [...questionData.options];
//     shuffleArray(shuffledOptions);
  
//     for (let i = 0; i < shuffledOptions.length; i++) {
//       const option = document.createElement('label');
//       option.className = 'option';
  
//       const radio = document.createElement('input');
//       radio.type = 'radio';
//       radio.name = 'quiz';
//       radio.value = shuffledOptions[i];
  
//       const optionText = document.createTextNode(shuffledOptions[i]);
  
//       option.appendChild(radio);
//       option.appendChild(optionText);
//       optionsElement.appendChild(option);
//     }
  
//     quizContainer.innerHTML = '';
//     quizContainer.appendChild(questionElement);
//     quizContainer.appendChild(optionsElement);
//   }
  
//   function checkAnswer() {
//     const selectedOption = document.querySelector('input[name="quiz"]:checked');
//     if (selectedOption) {
//       const answer = selectedOption.value;
//       if (answer === quizData[currentQuestion].answer) {
//         score++;
//       } else {
//         incorrectAnswers.push({
//           question: quizData[currentQuestion].question,
//           incorrectAnswer: answer,
//           correctAnswer: quizData[currentQuestion].answer,
//         });
//       }
//       currentQuestion++;
//       selectedOption.checked = false;
//       if (currentQuestion < quizData.length) {
//         displayQuestion();
//       } else {
//         displayResult();
//       }
//     }
//   }
  
//   function displayResult() {
//     quizContainer.style.display = 'none';
//     submitButton.style.display = 'none';
//     retryButton.style.display = 'inline-block';
//     showAnswerButton.style.display = 'inline-block';
//     resultContainer.innerHTML = `You scored ${score} out of ${quizData.length}!`;
//   }
  
//   function retryQuiz() {
//     currentQuestion = 0;
//     score = 0;
//     incorrectAnswers = [];
//     quizContainer.style.display = 'block';
//     submitButton.style.display = 'inline-block';
//     retryButton.style.display = 'none';
//     showAnswerButton.style.display = 'none';
//     resultContainer.innerHTML = '';
//     displayQuestion();
//   }
  
//   function showAnswer() {
//     quizContainer.style.display = 'none';
//     submitButton.style.display = 'none';
//     retryButton.style.display = 'inline-block';
//     showAnswerButton.style.display = 'none';
  
//     let incorrectAnswersHtml = '';
//     for (let i = 0; i < incorrectAnswers.length; i++) {
//       incorrectAnswersHtml += `
//         <p>
//           <strong>Question:</strong> ${incorrectAnswers[i].question}<br>
//           <strong>Your Answer:</strong> ${incorrectAnswers[i].incorrectAnswer}<br>
//           <strong>Correct Answer:</strong> ${incorrectAnswers[i].correctAnswer}
//         </p>
//       `;
//     }
  
//     resultContainer.innerHTML = `
//       <p>You scored ${score} out of ${quizData.length}!</p>
//       <p>Incorrect Answers:</p>
//       ${incorrectAnswersHtml}
//     `;
//   }
  
//   submitButton.addEventListener('click', checkAnswer);
//   retryButton.addEventListener('click', retryQuiz);
//   showAnswerButton.addEventListener('click', showAnswer);
  
//   displayQuestion();


// courses js

// let btn_a = document.querySelector("#a");
// let btn_b = document.querySelector("#b");
// let btn_c = document.querySelector("#c");
// let btn_d = document.querySelector("#d");
// let cancel1 = document.querySelector("#cross-a");
// let cancel2 =  document.querySelector("#cross-b");
// let cancel3 = document.querySelector("#cross-c");
// let cancel4 =  document.querySelector("#cross-d");

// btn_a.addEventListener("click", () => {
//     document.querySelector(".overlay").classList.add("overlay-nt");
//     document.querySelector(".popup_a").classList.add("popup_a-after");
// });
// cancel1.addEventListener("click", () => {
//     document.querySelector(".overlay").classList.remove("overlay-nt");
//     document.querySelector(".popup_a").classList.remove("popup_a-after");
// });

// btn_b.addEventListener("click", () => {
//     document.querySelector(".overlay").classList.add("overlay-nt");
//     document.querySelector(".popup_b").classList.add("popup_b-after");
// });
// cancel2.addEventListener("click", () => {
//     document.querySelector(".overlay").classList.remove("overlay-nt");
//     document.querySelector(".popup_b").classList.remove("popup_b-after");
// });

// btn_c.addEventListener("click", () => {
//     document.querySelector(".overlay").classList.add("overlay-nt");
//     document.querySelector(".popup_c").classList.add("popup_c-after");
// });
// cancel3.addEventListener("click", () => {
//     document.querySelector(".overlay").classList.remove("overlay-nt");
//     document.querySelector(".popup_c").classList.remove("popup_c-after");
// });

// btn_d.addEventListener("click", () => {
//     document.querySelector(".overlay").classList.add("overlay-nt");
//     document.querySelector(".popup_d").classList.add("popup_d-after");
// });
// cancel4.addEventListener("click", () => {
//     document.querySelector(".overlay").classList.remove("overlay-nt");
//     document.querySelector(".popup_d").classList.remove("popup_d-after");
// });



