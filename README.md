<p align="center"><h1 align="center">CrewAI: Linkedin Post Generation</h1></p>
<p align="center">
	<em>Crafting Your Voice, Amplifying Your Professional Impact</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/HopMaster03/linkedin-post-generation-CrewAI?style=default&logo=opensourceinitiative&logoColor=white&color=2b92ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/HopMaster03/linkedin-post-generation-CrewAI?style=default&logo=git&logoColor=white&color=2b92ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/HopMaster03/linkedin-post-generation-CrewAI?style=default&color=2b92ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/HopMaster03/linkedin-post-generation-CrewAI?style=default&color=2b92ff" alt="repo-language-count">
</p>
<p align="center"><!-- default option, no dependency badges. -->
  Developed with the following tools:
</p>
<p align="center">
	<!-- default option, no dependency badges. -->
  <img src="https://img.shields.io/badge/Streamlit-%23FE4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white">
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
</p>
<br>

##  Table of Contents

- [ Overview](#overview)
- [ Features](#-features)
- [ Project Structure](#-project-structure)
  - [ Project Index](#-project-index)
- [ Getting Started](#-getting-started)
  - [ Prerequisites](#-prerequisites)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
  - [ Testing](#-testing)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)

---

##  Overview

The linkedin-post-generation-CrewAI project revolutionizes LinkedIn content creation by automating personalized post generation. Leveraging advanced AI, it analyzes organizational data to craft posts that resonate with specific audiences, enhancing engagement and visibility. Ideal for marketers and social media managers, this tool streamlines content strategy and optimizes online presence.

---

##  Features

|      | Feature         | Summary       |
| :--- | :---:           | :---          |
| ⚙️  | **Architecture**  | <ul><li>Utilizes a modular approach with separate files for different functionalities like `app.py` for the interface and `crew.py` for team configuration.</li><li>Integrates data analysis and LinkedIn post generation within a single framework.</li><li>Supports environmental variables and PDF reading for dynamic content generation.</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Code is organized into distinct modules for clarity and maintainability.</li><li>Uses Python extensively, evident from the `.py` files and Python-based dependencies.</li><li>Adheres to a structured format in YAML files for configuration.</li></ul> |
| 📄 | **Documentation** | <ul><li>Documentation includes installation and usage commands.</li><li>File-specific documentation helps understand individual components' roles.</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Integrates with various Python libraries such as `beautifulsoup4` for web scraping and `selenium` for browser automation.</li><li>Uses `streamlit` for web app development, enabling interactive user interfaces.</li><li>Employs `undetected-chromedriver` for improved scraping capabilities without detection.</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Highly modular with separate configuration files (`agents.yaml` and `tasks.yaml`) for team roles and tasks.</li><li>Separation of concerns is evident with distinct scripts for different functionalities.</li><li>Modular design aids in easy scalability and maintenance of the codebase.</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Use of `undetected-chromedriver` and `selenium` suggests an emphasis on reliable and efficient data scraping.</li></ul> |
| 🛡️ | **Security**      | <ul><li>Utilizes `python-dotenv` for environment variable management, enhancing security by protecting API keys and other sensitive data.</li></ul> |

---

##  Project Structure

```sh
└── linkedin-post-generation-CrewAI/
    ├── LICENSE
    ├── Nike_logs.txt
    ├── app.py
    ├── config
    │   ├── agents.yaml
    │   └── tasks.yaml
    ├── crew.py
    ├── requirements.txt
    └── tools
        ├── linkedin_tools.py
        └── utils.py
```


###  Project Index
<details open>
	<summary><b><code>LINKEDIN-POST-GENERATION-CREWAI/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/HopMaster03/linkedin-post-generation-CrewAI/blob/master/Nike_logs.txt'>Nike_logs.txt</a></b></td>
				<td>- The file "Nike_logs.txt" within the project serves as a detailed log for data analysis tasks performed by an agent identified as a Data Analyst and Audience Researcher<br>- The primary function of this file is to document the analysis of input data concerning organizational details, specifically focusing on The Coca-Cola Company<br>- The log entry outlines the company's global presence, product portfolio, and sustainability initiatives, providing a comprehensive overview of the company's business operations and strategic focus areas.

This file is crucial for maintaining a record of the data analysis activities, which could be used for auditing, tracking progress, or further analysis in future projects<br>- It supports the broader architecture of the project by ensuring that detailed, timestamped data analysis activities are recorded, thereby enhancing transparency and accountability within the data management process<br>- This log file likely interacts with other components of the project that require insights from data analysis for decision-making or strategy development.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/HopMaster03/linkedin-post-generation-CrewAI/blob/master/app.py'>app.py</a></b></td>
				<td>- App.py serves as the interface for a LinkedIn post generator, enabling users to input organizational details and preferences to craft tailored posts<br>- It integrates environmental variables, PDF reading for context extraction, and leverages the LinkedInPostCrew module for generating posts based on emotional appeal and content type specified by the user.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/HopMaster03/linkedin-post-generation-CrewAI/blob/master/requirements.txt'>requirements.txt</a></b></td>
				<td>- Manages the dependencies required for the project, ensuring compatibility and functionality across various modules<br>- It includes libraries for web app development, AI integration, language processing, environment management, data manipulation, web scraping, and PDF handling, supporting the project's diverse needs in data analysis, AI-driven insights, and user interface creation.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/HopMaster03/linkedin-post-generation-CrewAI/blob/master/crew.py'>crew.py</a></b></td>
				<td>- Crew.py establishes a specialized team, the LinkedIn Post Crew, designed to enhance LinkedIn content strategy through a series of defined roles and tasks<br>- It configures agents like content strategists and SEO optimizers and assigns them specific tasks such as content creation and optimization, all managed within a sequential process framework.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- config Submodule -->
		<summary><b>config</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/HopMaster03/linkedin-post-generation-CrewAI/blob/master/config/tasks.yaml'>tasks.yaml</a></b></td>
				<td>- Configures tasks for a LinkedIn content strategy project, detailing processes from data collection and audience profiling to content creation and optimization<br>- It guides the collection of organizational insights, audience analysis, drafting and refining LinkedIn posts, integrating emotional appeals, and optimizing content for enhanced visibility and engagement on the platform.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/HopMaster03/linkedin-post-generation-CrewAI/blob/master/config/agents.yaml'>agents.yaml</a></b></td>
				<td>- Defines roles and objectives for team members involved in LinkedIn content creation, including a Project Manager, Data Analyst, Content Creator, and SEO Specialist<br>- Each role is detailed with specific goals and professional backgrounds, ensuring a structured approach to producing high-quality, targeted, and optimized LinkedIn posts.</td>
			</tr>
			</table>
		</blockquote>
	</details>
</details>

---
##  Getting Started

###  Prerequisites

Before getting started with linkedin-post-generation-CrewAI, ensure your runtime environment meets the following requirements:

- **Programming Language:** python
- **Package Manager:** pip


###  Installation

Install linkedin-post-generation-CrewAI using one of the following methods:

**Build from source:**

1. Clone the linkedin-post-generation-CrewAI repository:
```sh
❯ git clone https://github.com/HopMaster03/linkedin-post-generation-CrewAI
```

2. Navigate to the project directory:
```sh
❯ cd linkedin-post-generation-CrewAI
```

3. Install the project dependencies:


**Using `pip`** &nbsp;

```sh
❯ pip install -r requirements.txt
```

4. Create Environment variables:
```sh
LINKEDIN_EMAIL="your linkedin email"
LINKEDIN_PASSWORD="password for linkedin email"
LANGTRACE_API_KEY="langtrace_api_key"
OPENAI_API_KEY="openai_api_key"
```




###  Usage
Run linkedin-post-generation-CrewAI using the following command:
**Using `pip`** &nbsp;

```sh
streamlit run app.py
```

---
##  Project Roadmap

- [X] **`Task 1`**: <strike>Generate a personalized post.</strike>
- [ ] **`Task 2`**: Generate an image according to the content.
- [ ] **`Task 3`**: Integrate in content creation pipelines.

---

##  Contributing

- **💬 [Join the Discussions](https://github.com/HopMaster03/linkedin-post-generation-CrewAI/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/HopMaster03/linkedin-post-generation-CrewAI/issues)**: Submit bugs found or log feature requests for the `linkedin-post-generation-CrewAI` project.
- **💡 [Submit Pull Requests](https://github.com/HopMaster03/linkedin-post-generation-CrewAI/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/HopMaster03/linkedin-post-generation-CrewAI
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/HopMaster03/linkedin-post-generation-CrewAI/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=HopMaster03/linkedin-post-generation-CrewAI">
   </a>
</p>
</details>

---

##  License

This project is protected under the [MIT](https://choosealicense.com/licenses/mit/) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.



