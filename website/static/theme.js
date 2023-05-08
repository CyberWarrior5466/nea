systemTheme = () => {
  return window.matchMedia("(prefers-color-scheme: dark)").matches
    ? "dark"
    : "light";
};

currentTheme = () => {
  return document.documentElement.getAttribute("data-bs-theme");
};

/**
 * @param {"light" | "dark"} theme
 */
invert = (theme) => {
  return theme === "light" ? "dark" : "light";
};

/**
 * @param {"light" | "dark"} theme
 */
setTheme = (theme) => {
  // sets current theme to system preference
  document.documentElement.setAttribute("data-bs-theme", theme);
  window.monaco.editor.setTheme("vs-" + theme)
};


document.onreadystatechange = () => {
  if (localStorage.getItem("theme") === "light") {
    setTheme("light")
  } else if (localStorage.getItem("theme") == "dark") {
    setTheme("dark")
  } else {
    setTheme(systemTheme())
  }
};

window
  .matchMedia("(prefers-color-scheme: dark)")
  .addEventListener("change", () => {
    setTheme(systemTheme());
  });

changeTheme = () => {
  if (currentTheme() === systemTheme()) {
    localStorage.setItem("theme", invert(currentTheme()));
  } else {
    localStorage.removeItem("theme");
  }

  setTheme(invert(currentTheme()));
};