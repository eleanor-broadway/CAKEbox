---
title: Add your own resources
tags: [Central themes, Resources]
---

<!-- Visualising as sticky notes -->

<!-- Turn this into lines rather than notes -->

<div class="resource-layout">

  {% for resource in resources() %}
    <div class="resource-box">
      <div class="note-title">
        {{ resource.title }}
      </div>

      <div class="note-url">
        <a href="{{ resource.url }}" target="_blank" rel="noopener noreferrer">
        {{ resource.url }}     
      </div>

      <div class="note-text">
        {{ resource.comment }}
      </div>
    </div>

{% endfor %}

</div>


<!-- Box for users to submit a new resource -->
<div class="submit-box">

  <p class="submit-description">
    Share a resource.
  </p>

  <p class="submit-helper">
    </br>
    After clicking <strong>Submit</strong>, a GitHub issue will open
    with your resource pre-filled. Simply click <strong>"Create"</strong>
    to send it to the CAKE team for review before it goes live.
  </p>

  <input
    class="tip-input"
    id="resource-title"
    placeholder="Title"
  />

  <input
    class="tip-input"
    id="resource-url"
    placeholder="Paste the link to the resource here"
  />

  <textarea
    class="tip-textarea"
    id="resource-comment"
    placeholder="Tell us a bit about why you want to share this resource?"
  ></textarea>

<!-- <label for="resource-theme">Theme</label> -->

<!-- TO DO: Make this look nicer -->
<select id="resource-theme" onchange="toggleCustomTheme()">

  <option value="">Select a theme...</option>

  {% for theme in resource_themes() %}
    <option value="{{ theme }}">
      {{ theme | replace("-", " ") | title }}
    </option>
  {% endfor %}

  <option value="other">Other — create a new theme</option>

</select>

<input
  id="custom-theme"
  class="tip-input"
  placeholder="Enter a new theme"
  style="display: none;"
/>

  <button
    class="tip-submit-btn"
    onclick="submitResource()">
    Submit
  </button>
  </div>

</div>







<!-- Script that takes the user input and creates the issue -->
<script>
function toggleCustomTheme() {


//  Pretty sure this is working because if I manually create themes, these show up in the drop down as expected. 
  const themeSelect =
    document.getElementById("resource-theme");

  const customTheme =
    document.getElementById("custom-theme");

  if (themeSelect.value === "other") {
    customTheme.style.display = "block";

  } else {
    customTheme.style.display = "none";
    customTheme.value = "";

  }
}


function submitResource() {

  const title =
    document.getElementById("resource-title").value.trim();

    let url = document
    .getElementById("resource-url")
    .value
    .trim();

    if (!url.startsWith("http://") && !url.startsWith("https://")) {
    url = "https://" + url;
    }

  const url =
    document.getElementById("resource-url").value.trim();

  const comment =
    document.getElementById("resource-comment").value.trim();

  const selectedTheme =
    document.getElementById("resource-theme").value;

  let theme;

  if (selectedTheme === "other") {

    theme =
      document
        .getElementById("custom-theme")
        .value
        .trim()
        .toLowerCase()
        .replace(/\s+/g, "-");

  } else {
    theme = selectedTheme;
  }





  if (!title || !url || !comment || !theme) {
    alert("Please fill in all fields.");
    return;
  }

  const issueTitle =
    `[Resource:${theme}] ${title}`;

  const issueBody =
`title: ${title}
url: ${url}
comment: ${comment}
theme: ${theme}`;

  const githubUrl =
    "https://github.com/eleanor-broadway/CAKEbox/issues/new"
    + "?labels=resource-submission"
    + "&title=" + encodeURIComponent(issueTitle)
    + "&body=" + encodeURIComponent(issueBody);

  window.open(githubUrl, "_blank");
}

</script>
