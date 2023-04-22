import random
import webbrowser

input_file = "domain-names.txt" #found on https://www.whoisdownload.com/newly-registered-domains

filter_words = input("Enter filter words separated by comma (e.g. microsoft,support,tech..): ").split(",")

num_links = "1"

with open(input_file, "r") as f_in, open("filtered_links.html", "w") as f_out:
    
    f_out.write('<html>\n')
    f_out.write('<head>\n')
  
    f_out.write('<style>\n')
    f_out.write('body { font-family: Arial, sans-serif; }\n')
    f_out.write('h1 { text-align: center; }\n')
    f_out.write('form { display: flex; flex-direction: column; align-items: center; }\n')
    f_out.write('label { margin-bottom: 10px; }\n')
    f_out.write('input[type="text"] { padding: 5px; margin-bottom: 10px; }\n')
    f_out.write('button { padding: 10px 20px; background-color: #4CAF50; color: white; border: none; border-radius: 4px; cursor: pointer; }\n')
    f_out.write('a { display: block; margin-bottom: 10px; }\n')
    f_out.write('</style>\n')
    f_out.write('</head>\n')
    f_out.write('<body>\n')
    f_out.write('<h1>Filtered Links</h1>\n')
    f_out.write('<form>\n')
    f_out.write(f'<label for="num-links">Number of links to open:</label>\n')
    f_out.write(f'<input type="text" id="num-links" value="{num_links}">\n')
    f_out.write('<button onclick="openLinks()">Open Links</button>\n')
    f_out.write('</form>\n')

  
    lines = f_in.readlines()


    link_count = 0

   
    for line in random.sample(lines, len(lines)):
      
        line = line.strip()

      
        if any(word in line for word in filter_words):
       
            line = "https://www." + line

          
            f_out.write(f'<a href="{line}" target="_blank">{line}</a>\n')

           
            link_count += 1

    f_out.write(f'<p>{link_count} links found</p>\n')

 
    f_out.write('<script>\n')
    f_out.write('function openLinks() {\n')
    f_out.write('  var numLinks = document.getElementById("num-links").value;\n')
    f_out.write('  var links = Array.from(document.getElementsByTagName("a"));\n')
    f_out.write('  var shuffledLinks = links.sort(() => 0.5 - Math.random());\n')
    f_out.write('  for (var i = 0; i < numLinks && i < shuffledLinks.length; i++) {\n')
    f_out.write('    window.open(shuffledLinks[i].href);\n')
    f_out.write('    shuffledLinks[i].classList.add("visited");\n')
    f_out.write('    shuffledLinks[i].removeAttribute("onclick");\n')
    f_out.write('  }\n')
    f_out.write('}\n')
    f_out.write('</script>\n')

    
    f_out.write('<style>\n')
    f_out.write('a.visited {\n')
    f_out.write('  color: gray;\n')
    f_out.write('  text-decoration: line-through;\n')
    f_out.write('}\n')
    f_out.write('</style>\n')

 
    f_out.write('</body></html>\n')


print("Filtered links have been written to filtered_links.html")


import webbrowser
webbrowser.open('filtered_links.html')
