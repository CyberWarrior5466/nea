// setup monaco editor

require.config({ paths: { vs: "vs" } });

require(["vs/editor/editor.main"], function () {
  window.editor = monaco.editor.create(
    document.getElementById("monaco-editor"),
    {
      value: ["FOR i <- 1 TO 3", "    OUTPUT i", "ENDFOR"].join("\n"),
      automaticLayout: true,
    }
  );
});


// make request to /api/run
/**
 * Represents a book.
 * @param {boolean} flag
 */
async function request(flag) {
  const code = window.editor.getValue();

  return await fetch(
    document.URL + document.URL.endsWith("/") ? "api/run" : "/api/run",
    {
      method: "POST",
      headers: {
        accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ code: code, transpile: flag }),
    }
  ).then((response) => response.json());
}

run = () => {
  // replace \n with <br> from https://stackoverflow.com/a/5076492
  request(false).then(
    (value) =>
    (document.getElementById("output").innerHTML =
      document.getElementById("output").innerHTML + "> " +
      value.replace(/\n/g, "<br>"))
  );
};

transpile = () => {
  // replace \n with <br> from https://stackoverflow.com/a/5076492
  request(true).then(
    (value) =>
    (document.getElementById("output").innerHTML =
      document.getElementById("output").innerHTML +
      value.replace(/\n/g, "<br>"))
  );
};

clearOutput = () => {
  document.getElementById("output").innerHTML = ""
};
