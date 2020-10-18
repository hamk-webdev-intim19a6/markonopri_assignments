function answer(event) {
    var x = [];
    var total = 0;
    let answers = $(":checked");
    for (var answer of answers) {
        var idMatch = answer.id.match(/question-(\d+)-(\d+)/);
        var questionN = idMatch[1];
        var choiceN = idMatch[2];
        var points = questions[questionN].choices[choiceN].points;
        //console.log(answer.id, points);   will show answer.id and points.
        x.push(points);
        
    }
    total = x[0] + x[1] + x[2]    // total result of points.
    //console.log(total);       // debug for totalpoints.

    // JSON format for points
    var myObj, i, y = "";
    myObj = {
        "items":{
        "question1":x[0],
        "question2":x[1],
        "question3":x[2],
        "totalPoints":total
        }
    }
    // for loop for listing myObj
    for (i in myObj.items) {
       y += myObj.items[i] + " points\n";
       
    }
    console.log(myObj); // indicate points to console
    
    event.preventDefault();
    return false;
}
let form = "<form>\n";
for (let [questionN, question] of questions.entries()) {
    form += `<p>${question.text}<\/p>`;
    form += `<fieldset data-role="controlgroup" data-type="vertical">\n`;
    for (let [choiceN, choice] of question.choices.entries()) {
        form += `<input type="radio" id="question-` +
            `${questionN}-${choiceN}" name="question-${questionN}" ` +
            `value="${choiceN}">`;
        form += `<label for="question-${questionN}-${choiceN}">` +
            `${choice.text}<\/label>\n`;
        choiceN++;
    }
    form += `</fieldset>\n`;
    questionN++;
}
form += '<button class="ui-btn ui-shadow" onclick="answer(event)">' +
    'Answer<\/button>';
form += "<\/form>\n";
document.getElementById("container").innerHTML = form;