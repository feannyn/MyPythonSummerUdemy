// PART 4 ARRAY EXERCISE
// This is  a .js file with commented hints, its optional to use this.

// Create Empty Student Roster Array
// This has been done for you!
var roster = [];
// Create the functions for the tasks

// ADD A NEW STUDENT

// Create a function called addNew that takes in a name
// and uses .push to add a new student to the array

function addNew(name)
{
	roster.push(name);
}


// REMOVE STUDENT
function remove(name)
{
	index = roster.indexOf(name);

	if(index > -1)
	{
		roster.splice(index, 1);
	}
}
// Create a function called remove that takes in a name
// Finds its index location, then removes that name from the roster

// HINT: http://stackoverflow.com/questions/5767325/how-to-remove-a-particular-element-from-an-array-in-javascript
//

// DISPLAY ROSTER

// Create a function called display that prints out the orster to the console.
function display()
{
	console.log(roster);
}

// Start by asking if they want to use the web app
var choice = prompt("Would you like to use the web application?")
// Now create a while loop that keeps asking for an action (add,remove, display or quit)
// Use if and else if statements to execute the correct function for each command.
if(choice === "yes")
{
	while(choice != "quit")
	{
		choice = prompt("Please enter a valid action(add, remove, display, quit): ");

		if(choice === "add")
		{
			student = prompt("Please enter a student name: ");
			console.log("To be added:" + student);
			addNew(student);
		}
		else if(choice === "remove")
		{
			student = prompt("Please enter a student you wish to remove: ");
			console.log("to be removed: " + student);
			remove(student);
		}
		else if(choice === "display")
		{
			display();
		}
	}
}
alert("Have a nice day!");




