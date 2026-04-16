async function checkSimilarity() {
    const code1 = document.getElementById("code1").value;
    const code2 = document.getElementById("code2").value;

    const response = await fetch("http://127.0.0.1:8000/check", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            codes: [code1, code2]
        })
    });

    const data = await response.json();
    let similarity = data.similarity_matrix[0][1] * 100;

    document.getElementById("result").innerText =
        "Similarity: " + similarity.toFixed(2) + "%";

    highlightLines(code1, code2);
}


// 🔥 Highlight matching lines
function highlightLines(code1, code2) {
    const lines1 = code1.split("\n");
    const lines2 = code2.split("\n");

    let result = "";

    lines1.forEach(line => {
        if (lines2.includes(line.trim())) {
            result += `<span style="color:red; font-weight:bold">${line}</span>\n`;
        } else {
            result += line + "\n";
        }
    });

    document.getElementById("highlight").innerHTML = result;
}