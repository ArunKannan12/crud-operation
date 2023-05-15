const forms = document.querySelector(".forms"),
pwShowHide1 = document.querySelectorAll(".pass1")
pwShowHide2 = document.querySelectorAll(".pass2")
links = document.querySelectorAll(".link");

pwShowHide1.forEach(eyeIcon => {
eyeIcon.addEventListener("click", () => {
  let pwFields = eyeIcon.parentElement.parentElement.querySelectorAll(".password1");
  
  pwFields.forEach(password => {
      if(password.type === "password"){
          password.type = "text";
          eyeIcon.classList.replace("bx-hide", "bx-show");
          return;
      }
      password.type = "password";
      eyeIcon.classList.replace("bx-show", "bx-hide");
  })
  
})
})      
pwShowHide2.forEach(eyeIcon => {
    eyeIcon.addEventListener("click", () => {
      let pwFields = eyeIcon.parentElement.parentElement.querySelectorAll(".password2");
      
      pwFields.forEach(password => {
          if(password.type === "password"){
              password.type = "text";
              eyeIcon.classList.replace("bx-hide", "bx-show");
              return;
          }
          password.type = "password";
          eyeIcon.classList.replace("bx-show", "bx-hide");
      })
      
    })
    }) 

// links.forEach(link => {
// link.addEventListener("click", e => {
//  e.preventDefault(); //preventing form submit
//  forms.classList.toggle("show-signup");
// })
// })