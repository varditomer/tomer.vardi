function refreshPage(){
    window.location.reload();
}

// function hand() {
//   var a;
//   a = document.getElementById("div1");
//   a.innerHTML = "&#xf25a;";
//   setTimeout(function () {
//       a.innerHTML = "&#xf256;";
//     }, 500);
//   setTimeout(function () {
//       a.innerHTML = "&#xf259;";
//     }, 1000);
//   setTimeout(function () {
//       a.innerHTML = "&#xf256;";
//     }, 1500);
// }
//
// hand();
// setInterval(hand, 2000);


fetch('https://reqres.in/api/users?page=2').then(
    response => response.json()
).then(
    responseJSON => createUsersList(responseJSON.data)
).catch(err => console.log(err));

function createUsersList(users) {
    console.log(users);
    const user = users[0];
    console.log(user);
    const curr_main = document.querySelector("main");
    for (let user of users) {
        const section = document.createElement('section');
        section.innerHTML = `
            <img src="${user.avatar}" alt="Profile_Avatar"/>
            <div>
            <span>${user.first_name} ${user.last_name}</span><br>
            <a href="mailto:${user.email}">Send Email</a>
            </div>`;
    curr_main.appendChild(section);
    }
}


