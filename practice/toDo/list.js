var todos = ["Buy new turtle"];

var input = prompt("What would you like to do?");


while (input != "quit"){

    if (input == "list"){
        listTodos();
        
    }else if(input == "new"){
        addTodo();
    }
    else if(input === "delete"){
        deleteTodo();
    }
    input = prompt("What would you like to do?");
}

console.log("Done with the app.")


function listTodos(){
    console.log("*******************");
        todos.forEach(function(todo, i){
            console.log(i + ": " + todo);
        })
    console.log("*******************");
}

function addTodo(){
    var newTodo = prompt("Enter new todo");
    todos.push(newTodo);
    console.log("Added Todo");
}

function deleteTodo(){
    var index = prompt("Enter index of todo to delete: ");
    //splice() will point to index value and delete n values after that value. 
    todos.splice(index,1);
    console.log("Delete Todo");
}