Find environments for courses
====

.. raw:: html

    <div class="input-group mb-3">
        <input type="text" class="form-control" id="searchInput" placeholder="Search courses..." aria-label="Search courses">
    </div>
    <script>
        window.addEventListener('DOMContentLoaded', function() {
            const urlParams = new URLSearchParams(window.location.search);
            const searchValue = urlParams.get('search') || '';
            const searchInput = document.getElementById('searchInput');
            searchInput.value = searchValue;

            const items = document.querySelectorAll('[data-environment]');
            items.forEach(item => {
                const name = item.getAttribute('data-environment').toLowerCase();
                if (name.includes(searchValue) && (searchValue.length !== 0)) {
                    item.style.display = '';
                } else {
                    item.style.display = 'none';
                }
            });
        });
        document.getElementById('searchInput').addEventListener('input', function() {
            const searchValue = this.value.toLowerCase();
            const items = document.querySelectorAll('[data-environment]');
            const url = new URL(window.location);
            url.searchParams.set('search', searchValue);
            window.history.replaceState({}, '', url);
            items.forEach(item => {
                const name = item.getAttribute('data-environment').toLowerCase();
                if (name.includes(searchValue) && (searchValue.length !== 0)) {
                    item.style.display = '';
                } else {
                    item.style.display = 'none';
                }
            });
        });
    </script>


.. raw:: html

    {% for course_name, years in environments.items() %}
    <div data-environment="{{course_name}}" style="display: none;">
        <h3>{{course_name}}</h3>
        {% for year, metadata in years.items() %}
            <details class="sd-sphinx-override sd-dropdown sd-card sd-mb-3">
                <summary class="sd-summary-title sd-card-header">
                    <span class="sd-summary-text">{{metadata.course_year}}</span>
                    <span class="sd-summary-state-marker sd-summary-chevron-right">
                        <svg version="1.1" width="1.5em" height="1.5em" class="sd-octicon sd-octicon-chevron-right" viewBox="0 0 24 24" aria-hidden="true">
                            <path d="M8.72 18.78a.75.75 0 0 1 0-1.06L14.44 12 8.72 6.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018l6.25 6.25a.75.75 0 0 1 0 1.06l-6.25 6.25a.75.75 0 0 1-1.06 0Z"></path>
                        </svg>
                    </span>
                </summary>
                <div class="sd-summary-content sd-card-body docutils">
                    <p>In order to install python requirements for {{course_name}} {{metadata.course_year}} do the following steps:</p>
                    <ol>
                        <li><p>Make sure that you have a conda installation on your PC. If you do not have a conda installation on your computer please follow the guide: <a href="#" onclick="PyS_redirectUser('../package-managed.html');">How To Install Python</a>.</p></li>
                        <li>
                            <p>Run the following command in a terminal to create a conda environment with all course requirements:</p>
                            <div class="highlight-bash notranslate"><div class="highlight">
                                <pre>conda create -f "{{metadata.env_path}}" -n "{{metadata.course_env_name}}"</pre>
                            </div></div>
                        </li>
                        <li>
                            <p>In order to use the environment you have activate it.</p>
                            <p><b>Jupyter notebook</b>: select "{{metadata.course_env_name}}" in the kernel selection:
                            <img alt="/_images/VSC-select-kernel.png" class="align-center" src="../../_images/VSC-select-kernel.png" style="width: 100%;"></p>

                            <p><b>.py file</b>: press <kbd class="kbd docutils literal notranslate">Ctrl</kbd> + <kbd class="kbd docutils literal notranslate">shift</kbd> + <kbd class="kbd docutils literal notranslate">P</kbd> type "Python: Select Interpreter" and press <kbd class="kbd docutils literal notranslate">enter</kbd>. Choose the option "{{metadata.course_env_name}}". </p>

                            <p><b>Terminal</b>: run the command:
                            <div class="highlight-bash notranslate"><div class="highlight">
                                <pre id="codecell_activate_{{metadata.course_env_name}}">conda activate "{{metadata.course_env_name}}"</pre>
                            </div></div> </p>
                        </li>
                        
                    <ol>
                </div>
            </details>
        {% endfor %}
        <hr/>
    </div>
    {% endfor %}

