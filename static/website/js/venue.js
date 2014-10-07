$(document).ready(function(){

var airport = '<iframe width="100%" height="100%" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://www.google.co.in/maps?f=d&amp;source=s_d&amp;saddr=Chhatrapati+Shivaji+International+Airport,+Andheri+East,+Mumbai,+Maharashtra&amp;daddr=IIT+Main+Gate&amp;hl=en&amp;geocode=FQFLIwEdg-NXBCGuqHTEYBrMHilHKb2ZUMjnOzGuqHTEYBrMHg%3BFRrUIwEdep5YBCldyp4n8sfnOzFZy8ueURQugA&amp;aq=4&amp;oq=IIT&amp;sll=19.099667,72.883154&amp;sspn=0.094407,0.154324&amp;mra=pd&amp;ie=UTF8&amp;t=m&amp;ll=19.110379,72.895527&amp;spn=0.029763,0.042183&amp;output=embed"></iframe>';
var airport_description = 'Convenient way to reach IITB from airport is to BEST buses running on route no. 382 or 409. Alternatively you may take an auto directly to IIT which would cost you around 90 rs.(depending on traffic) or a taxi which would cost around 100 Rs.';

var dadar = '<iframe width="100%" height="100%" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://www.google.co.in/maps?f=d&amp;source=s_d&amp;saddr=dadar+station&amp;daddr=IIT+Main+Gate&amp;hl=en&amp;geocode=FZMqIgEdYXRXBCkdh7S_3M7nOzHZNplA5uMmIw%3BFRrUIwEdep5YBCldyp4n8sfnOzFZy8ueURQugA&amp;aq=&amp;sll=19.037454,72.908363&amp;sspn=0.188885,0.308647&amp;mra=ls&amp;ie=UTF8&amp;ll=19.037454,72.908363&amp;spn=0.112729,0.100371&amp;t=m&amp;output=embed"></iframe>';
var dadar_description = 'Go to Dadar central line (typically on platform 6 of central line). Buy a ticket to Kanjurmarg at the ticket counter located on a level above the platform. Board a â€˜slowâ€™ local train (typically from platforms 3-5) which goes atleast upto Thane. Get down at Kanjurmarg Station (exit from platform No.1 to Kanjurmarg west). Take an auto rickshaw to IITB (Fare ~ Rs. 30).';

var thane = '<iframe width="100%" height="100%" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://www.google.co.in/maps?f=d&amp;source=s_d&amp;saddr=Thane+Railway+Station,+Station+Road+Kopri,+Thane,+Maharashtra&amp;daddr=IIT+Main+Gate&amp;hl=en&amp;geocode=FY7CJAEd_4BZBCkjQ1Rf37jnOzF9iI2abfvySQ%3BFRrUIwEdep5YBCldyp4n8sfnOzFZy8ueURQugA&amp;aq=4&amp;oq=IIT&amp;sll=19.155222,72.944412&amp;sspn=0.094375,0.154324&amp;mra=pd&amp;ie=UTF8&amp;ll=19.155222,72.944412&amp;spn=0.06341,0.058068&amp;t=m&amp;output=embed"></iframe>';
var thane_description = 'Buy a ticket to Kanjurmarg (central line) at the local train ticket counter. Come to platform 1, 3 or 4. Board a â€˜slowâ€™ local train which goes atleast upto Dadar/CST. Get down at Kanjurmarg Station (exit from platform No.1 to Kanjurmarg west). Take an auto rickshaw to IITB (Fare ~ Rs. 30).';

var bandra = '<iframe width="100%" height="100%" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://www.google.co.in/maps?f=d&amp;source=s_d&amp;saddr=Bandra+Terminus,+Naupada,+Bandra+East,+Mumbai,+Maharashtra&amp;daddr=IIT+Main+Gate&amp;hl=en&amp;geocode=FWLeIgEdQHdXBCm3sivHGcnnOzF9Gr08r3UTdQ%3BFRrUIwEdep5YBCldyp4n8sfnOzFZy8ueURQugA&amp;aq=0&amp;oq=Bandra+ter&amp;sll=19.155709,72.945614&amp;sspn=0.094375,0.154324&amp;mra=ls&amp;ie=UTF8&amp;ll=19.155709,72.945614&amp;spn=0.079966,0.075124&amp;t=m&amp;output=embed"></iframe>';
var bandra_description = 'Go to the Bandra terminus (BDTS), take an auto rickshaw to the Kurla Station (Fare ~ Rs. 40). Buy a ticket to Kanjurmarg (central line) at the local train ticket counter. Board a â€˜slowâ€™ local train (typically from platform No.1) which goes atleast upto Thane. Get down at Kanjurmarg Station (exit from platform No.1 to Kanjurmarg west). Take an auto rickshaw to IITB (Fare ~ Rs. 30).';

var tilak = '<iframe width="100%" height="100%" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://www.google.co.in/maps?f=d&amp;source=s_d&amp;saddr=Lokmanya+Tilak+Terminus,+Pipeline+Road,+Kurla,+Mumbai,+Maharashtra&amp;daddr=IIT+Main+Gate&amp;hl=en&amp;geocode=FSb7IgEdST5YBCGh8y-GNk5pZinbn-jom8jnOzGh8y-GNk5pZg%3BFRrUIwEdep5YBCldyp4n8sfnOzFZy8ueURQugA&amp;aq=0&amp;oq=Lokmany&amp;sll=19.101053,72.879009&amp;sspn=0.094406,0.154324&amp;mra=ls&amp;ie=UTF8&amp;ll=19.101053,72.879009&amp;spn=0.063015,0.045739&amp;t=m&amp;output=embed"></iframe>';
var tilak_description = 'The most convenient way to reach IITB is to take an auto rickshaw (Fare ~ Rs. 80).';

var central = '<iframe width="100%" height="100%" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://www.google.co.in/maps?f=d&amp;source=s_d&amp;saddr=Mumbai+Central+station,+Mumbai,+Maharashtra&amp;daddr=IIT+Main+Gate&amp;hl=en&amp;geocode=FVt4IQEd3SJXBCFssj0JqjsoWSmzxd6Nbs7nOzFssj0JqjsoWQ%3BFRrUIwEdep5YBCldyp4n8sfnOzFZy8ueURQugA&amp;aq=&amp;sll=19.0472,72.879606&amp;sspn=0.188874,0.308647&amp;mra=ls&amp;ie=UTF8&amp;t=m&amp;ll=19.0472,72.879606&amp;spn=0.163085,0.117661&amp;output=embed"></iframe>';
var central_description = 'Go to the Bombay Central Terminus (BCT) and walk to the Bombay Central local train. Buy a ticket to Kanjurmarg (central line) at the local train ticket counter. Board a â€˜slowâ€™ local train that halts at all stations on the line to Andheri/Borivali. Get down at Dadar (western line). Walk over to Dadar (central line) using an over-bridge. Further, kindly follow the instructions given earlier for Dadar (central line) to IITB.';

var shivaji = '<iframe width="100%" height="100% "src="https://www.google.com/maps/embed?pb=!1m21!1m12!1m3!1d26081603.294420466!2d-95.677068!3d37.06250000000001!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m6!1i0!3e6!4m1!2sCST%2C+Dadabhai+Naoroji+Road%2C+Chhatrapati+Shivaji+Terminus+Area%2C+Mumbai%2C+Maharashtra%2C+India!4m1!2sIIT+Main+Gate%2C+IIT+Area%2C+Mumbai%2C+Maharashtra%2C+India!5e0!3m2!1sen!2s!4v1395233704932" frameborder="0" style="border:0"></iframe>';
var shivaji_description = 'Buy a ticket to Kanjurmarg (central line) at the local train ticket counter. Come to the local train terminus (platforms 1-8, right of the long distance terminal). Board a â€˜slowâ€™ local train (typically from platforms 3-5) which goes atleast upto Thane. Get down at Kanjurmarg Station (exit from platform No.1 to Kanjurmarg west). Take an auto rickshaw to IITB (Fare ~ Rs. 30).';

  /* Load map on link click */
  $(".side-nav li a").click(function(e){
    
    var clicked = $(this).attr("id");
    var from = '';
    switch(clicked){
    	case "airport": 
            clicked = airport; 
            from = 'From Airport';
            description = airport_description;
            break;
    	case "dadar": 
            clicked = dadar;
            from = 'From Dadar Station';
            description = dadar_description;
            break;
    	case "thane": 
            clicked = thane;
            from = 'From Thane Station';
            description = thane_description;
            break;
    	case "bandra": 
            clicked = bandra;
            from = 'From Bandra Terminus';
            description = bandra_description;
            break;
    	case "tilak": 
            clicked = tilak;
            from = 'From Lokmanya Tilak Terminus';
            description = tilak_description;
            break;
    	case "central": 
            clicked = central;
            from = 'From Mumbai Central';
            description = central_description;
            break;
    	case "shivaji": 
            clicked = shivaji;
            from = 'From Chhatrapati Shivaji Terminus';
            description = shivaji_description;
            break;
    }
    $(".side-nav li").removeClass("active");
    $(this).closest('li').addClass("active");
    $("#from").html(from);
    $("#description").html(description);
    $("#mappy").html(clicked);
    e.preventDefault();
  });
});
