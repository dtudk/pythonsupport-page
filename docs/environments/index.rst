.. _environments-list:


Course specific conda environments
==================================

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


{% for course_number, course_periods in course_environments %}
{% set course_full_name = course_periods[-1].course_full_name %}
.. raw:: html

    <div data-environment="{{course_full_name}}">

.. dropdown:: {{course_full_name}}

    {% for metadata in course_periods %}
    :doc:`{{metadata.course_year}} {{metadata.course_semester}} </environments/course/{{metadata.course_env_name}}>`
    {% endfor %}

.. raw:: html

    <hr/>
    </div>
{% endfor %}
