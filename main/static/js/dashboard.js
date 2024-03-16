const search = document.querySelector("#submit");
const input = document.querySelector(".search");
const statuses = document.querySelector("#status");
const task = document.getElementById('tasks')
const counts = document.getElementById('counts')

let defaultUrl= 'taskcreate/'

GetTask(defaultUrl);
projectStatuses();


function SearchQuery(){
    search.addEventListener('click', function(e){
        e.preventDefault()
        var query = input.value.trim()
        console.log(query)
        if(!query){
            input.value = '';
            url = 'taskcreate/'
        } else{
            url = `taskcreate/?search=${query}`;
        };
        GetTask(url);
    })
}

function Filter() {
    statuses.addEventListener('change', function() {
        var query = statuses.value;
        console.log(query);
        if (!query){
            url = 'taskcreate/'
        }else{
            url = `taskcreate/?proj_status=${query}`;
        }        
        GetTask(url);
    });
}

function GetTask(url){
    $.ajax({
        url: url,
        type: 'GET',
        success: function(data){
            if (data.length === 0) {
                task.innerHTML = 'No tasks found.';
                counts.innerHTML = '0 results found'
            } else {
                counts.innerHTML = ''
                task.innerHTML = ''
                counts.append(`${data.length} results found`)
                data.forEach(function(task){
                    $('#tasks').append( `
                        <div class="mt-5 mb-5 h-[6em] text-sm font-medium text-center border-b text-gray-500 rounded-lg shadow-lg flex flex-row items-center justify-center dark:text-gray-400">
                            <div class="w-full focus-within:z-10 basis-1/2">                                    
                                <div class="inline-block w-full p-4 text-gray-900 shadow-inner rounded-s-lg">
                                    <img class="w-5 xl:w-7 h-5 xl:h-7 mt-2 rounded-full" src=" ${task.img} " alt="Jese image">
                                    <div class="xl:ps-10 ps-7 -mt-8 text-start">
                                        <div class="text-[0.85em] xl:text-sm font-bold text-black">${task.name}</div>
                                        <div class="font-medium xl:text-xs text-[0.7em] text-gray-400">${task.created}</div>
                                    </div>  
                                </div>
                            </div>

                            <div class="w-full focus-within:z-10 basis-1/4 h-[5.1em]">
                                <div class="inline-block w-full p-4 text-gray-800 shadow-inner py-auto">
                                    <button aria-disabled="true" class="bg-slate-100 py-1.5 px-4 rounded-lg items-center xl:text-xs text-[0.7em] font-bold"> ${task.readabletime}</button>
                                </div>
                            </div>

                            <div class="w-full focus-within:z-10 basis-1/4 h-[5.15em]">
                                <div class="w-full p-4 text-gray-900 shadow-inner flex flex-col text-[0.83em] xl:text-xs">
                                    <p>
                                        <b>90</b>/148
                                    </p>
                                    <small class="ml-0 xl:ml-9 text-gray-400 text-center xl:text-start">
                                        Tasks
                                    </small>
                                </div>
                            </div> 

                            <div class="w-full focus-within:z-10 basis-1/4 h-[5.19em]">
                                <div class="w-full p-4 text-gray-900 shadow-inner">
                                    <div class="flex items-center text-blue-300/75 gap-1.5 my-2 text-[0.6em] xl:text-xs">
                                        <svg class="w-4 h-4 text-blue-300/50" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
                                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 9h6m-6 3h6m-6 3h6M6.996 9h.01m-.01 3h.01m-.01 3h.01M4 5h16a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1Z"/>
                                        </svg>
                                        ${task.status}
                                    </div>
                                    <div class="max-w-24 w-full bg-blue-100 rounded-full h-1 mb-4 dark:bg-blue-100">
                                        <div class="bg-blue-300 h-1 rounded-full dark:bg-blue-300" style="width: 35%"></div>
                                    </div>
                                </div>
                            </div>

                            <div class="w-full focus-within:z-10 basis-1/4">
                                <div class="w-full h-[5.3em] p-4 text-gray-900 shadow-inner rounded-e-lg flex items-center">
                                    <div class="flex -space-x-3 rtl:space-x-reverse pr-2">
                                        <img class="w-5 xl:w-7 h-5 xl:h-7 border-2 border-white rounded-full dark:border-gray-800 bg-gray-500" src="/static/img/people.png" alt="">
                                        <img class="w-5 xl:w-7 h-5 xl:h-7 border-2 border-white rounded-full dark:border-gray-800" src="/static/img/capman.png" alt="">
                                        <img class="w-5 xl:w-7 h-5 xl:h-7 border-2 border-white rounded-full dark:border-gray-800" src="/static/img/avatar.png" alt="">
                                        <a class="flex items-center justify-center w-5 xl:w-7 h-5 xl:h-7 text-xs font-medium text-white bg-gray-700 border-2 border-white rounded-full hover:bg-gray-600 dark:border-gray-800" href="#">+3</a>
                                    </div>
                                    <div>
                                        <button id="dropdownMenuIconButton" data-dropdown-toggle="dropdownDots" data-dropdown-placement="bottom-start" class="inline-flex self-center z-30 items-center text-sm font-medium text-center text-gray-900 rounded-lg bg-transparent" type="button">
                                            <svg class="w-4 h-4 text-black dark:text-black" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 4 15">
                                                <path d="M3.5 1.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 6.041a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 5.959a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Z"/>
                                            </svg>
                                        </button>
                                        <div id="dropdownDots" class="z-90 hidden bg-white divide-y divide-gray-100 rounded-lg shadow w-40 dark:bg-gray-700 dark:divide-gray-600">
                                            <ul class="py-2 text-sm text-gray-700 dark:text-gray-200" aria-labelledby="dropdownMenuIconButton">
                                                <li>
                                                    <a href="#" class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">Reply</a>
                                                </li>
                                                <li>
                                                    <a href="#" class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">Forward</a>
                                                </li>
                                                <li>
                                                    <a href="#" class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">Copy</a>
                                                </li>
                                                <li>
                                                    <a href="#" class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">Report</a>
                                                </li>
                                                <li>
                                                    <a href="#" class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">Delete</a>
                                                </li>
                                            </ul>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>                        
                    `)
                })
            }            
            console.log(data)
            console.log(data.length)
        },
        error: function(rs, e){
            console.log(rs.error);
        },
    });
}


function projectStatuses() {
    $.ajax({
        url: 'projcreate/',
        type: 'GET',
        success: function(data){
            console.log(data)
            var selectDropdown = $('#status');
            selectDropdown.empty();

            selectDropdown.append($('<option>', {
                value: '',
                text: 'All'
            }));
            data.forEach(function(status){
                selectDropdown.append($('<option>', {
                    value: status.status,
                    text: status.status
                }));
            });
        },
        error: function(xhr, status, error){
            console.error("Error fetching project statuses:", error);
        }
    });
}


SearchQuery();
Filter();
    

    
