
function userByName(users) {
    users.sort(function(a, b) {
        return a.name - b.name;
    });
    console.log(users)
}

function userByAge(users) {
    users.sort(function(a, b) {
        return a.age - b.age;
    });
}
