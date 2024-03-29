import inquirer from "inquirer";
import axios from "axios";
import formdata from "form-data";

async function GetOperation() {
    const answer = await inquirer.prompt({
        type: "list", 
        name: "operation",
        message: "You didn't enter a valid operation. Please select an operation to perform.",
        choices: ["add", "delete", "search", "autocomplete", "display"]
    })
    return answer["operation"]
}

async function GetWord() {
    let answer = await inquirer.prompt({
        type: "input", 
        name: "word",
        message: "Please type the string required to perform the selected operation: "
    });

    while (answer["word"] == "" || answer["word"].replace(/[^A-Za-z]/g, '') == "") {
        answer = await inquirer.prompt({
            type: "input", 
            name: "word",
            message: "Word must include at least one valid (alphabetical) character! Please try again: "
        });
    };

    return answer["word"];
    
}

export async function CLI(args) {
    const VALID_OPS = new Set(["add", "delete", "search", "autocomplete", "display"]);

    // Take 2nd-onwards values of args (list), replace all nontext values, then convert to lowercase 
    args = args.splice(2).map(i => i.replace(/[^A-Za-z]/g, '').toLowerCase())

    let operation = ""
    let word = ""

    if (args.length > 0 && VALID_OPS.has(args[0])) {
        operation = args[0]
    } else {
        operation = await GetOperation();
    }

    if (args.length > 1 || operation == "display") {
        word = args[1] || ""
    } else {
        word = await GetWord();
    }

    const formData = new formdata();

    formData.append("string", word);
    axios.post("https://aydanpirani.pythonanywhere.com/"+operation, formData, {
     headers: formData.getHeaders()
    })
    .then(response => console.log(response.data))
    .catch(error => console.log(error))
}