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

    {% for course_name, years in ENVIRONMENTS.items() %}
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
                    <p>Run this command to create a conda environment for the course:</p>
                    <pre>conda create -f "{{metadata.env_path}}" -n "{{metadata.course_env_name}}"</pre>
                </div>
            </details>
        {% endfor %}
        <hr/>
    </div>
    {% endfor %}

