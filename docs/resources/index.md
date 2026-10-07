---
title: Add your own resources
tags: [Central themes, Resources]
---

<div class="resources-board">
  {% for resource in resources() %}
        <div class="resource-box">
            <div class="resource-title">
                {{ resource.title }}
            </div>
            <div class="resource-url">
                <a href="{{ resource.url }}">{{ resource.url }}</a>
            </div>
            <div class="resource-text">
                {{ resource.comment }}
            </div>
        </div>
    {% endfor %}
</div>


<!-- Box for users to submit a new resource -->
<div class="resources-submit-box">

  <p class="resources-submit-description">
    Have a resource to share?
  </p>

  <p class="resources-submit-helper">
    We'd love to hear about websites, tools, guides, or other resources you've found useful. Tell us a little about what makes it worth sharing.
  </p>

  <p class="resources-submit-helper">
    </br>
    After clicking <strong>Submit</strong>, a GitHub issue will open
    with your resource pre-filled. Simply click <strong>"Create"</strong>
    to send it to the CAKE team for review before it goes live.
  </p>

  <input
    class="tip-input"
    id="resource-title"
    placeholder="Resource title"
  />

  <input
    class="tip-input"
    id="resource-url"
    placeholder="Paste the resource link"
  />

  <textarea
    class="tip-textarea"
    id="resource-comment"
    placeholder="What makes this resource useful? Tell us a little about it..."
  ></textarea>

<label for="resource-theme">What theme does this resource fit under?</label>

<select id="resource-theme" onchange="toggleCustomTheme()">

  <option value="">Select a theme...</option>

  {% for theme in resource_themes() %}
    <option value="{{ theme }}">
      {{ theme | replace("-", " ") | title }}
    </option>
  {% endfor %}

  <option value="other">Other — suggest a new theme</option>

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



<!-- Script that takes the user input and creates the issue -->
<script>
function toggleCustomTheme() {
  const themeSelect = document.getElementById("resource-theme");
  const customTheme = document.getElementById("custom-theme");

  if (themeSelect.value === "other") {
    customTheme.style.display = "block";
  } else {
    customTheme.style.display = "none";
    customTheme.value = "";
  }
}

function submitResource() {
  const title = document
    .getElementById("resource-title")
    .value
    .trim();

  let url = document
    .getElementById("resource-url")
    .value
    .trim();

  const comment = document
    .getElementById("resource-comment")
    .value
    .trim();

  const selectedTheme = document
    .getElementById("resource-theme")
    .value;

  // Add https:// 
  if (url && !url.startsWith("http://") && !url.startsWith("https://")) {
    url = "https://" + url;
  }

  let theme;

  if (selectedTheme === "other") {
    theme = document
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

  if (!url.includes("www.")) {
    alert("Please enter a URL that includes www.");
    return;
  }
  
  const issueTitle = `[Resource:${theme}] ${title}`;

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