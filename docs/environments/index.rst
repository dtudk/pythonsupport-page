.. _environments-list:


Find environments for courses
====

.. raw:: html
    
    <input type="search" class="form-control env-search" id="searchInput" placeholder="Search courses..." aria-label="Search courses"> <br/>
    <script>
        window.addEventListener('DOMContentLoaded', function() {
            const urlParams = new URLSearchParams(window.location.search);
            const searchValue = urlParams.get('search') || '';
            const searchInput = document.getElementById('searchInput');
            searchInput.value = searchValue;

            const items = document.querySelectorAll('[data-environment]');
            items.forEach(item => {
                const name = item.getAttribute('data-environment').toLowerCase();
                if (name.includes(searchValue) || (searchValue.length == 0)) {
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
                if (name.includes(searchValue) || (searchValue.length == 0)) {
                    item.style.display = '';
                } else {
                    item.style.display = 'none';
                }
            });
        });
    </script>


{% for full_course_name, years in environments.items() %}
.. raw:: html
    
    <div data-environment="{{full_course_name}}">

.. dropdown:: {{full_course_name}}

    {% for year, metadata in years.items() %}
    `{{metadata.course_identifier}} <./course/{{metadata.course_env_name}}.html>`_
    {% endfor %}

.. raw:: html

    <hr/>
    </div>
{% endfor %}