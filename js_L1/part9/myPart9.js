var firstName = prompt("Please enter your first name:");
var lastName = prompt("now enter your last Name:");
var age = prompt("What is your age?");
var height = prompt("How tall are you?(in centimeters)");
var pet = prompt("What is your pets' name?");


if(firstName[0] == lastName[0])
{
	if(age > 20 && age < 30)
	{
		if(height >= 170)
		{
			if(pet[pet.length - 1] === "y")
			{
				console.log("welcome comrade, you gained access");
			}
		}
	}
}
else
	console.log("Nothing to see here....");