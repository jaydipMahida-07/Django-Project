from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from blog.models import Category, Article
from profiles.models import Profile
import random

User = get_user_model()

class Command(BaseCommand):
    help = 'Seeds the database with actual readable data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding real data...')
        
        # 1. Clean up old placeholder data
        # 1. Clean up old placeholder data
        self.stdout.write('Deleting all existing articles to ensure fresh seed...')
        Article.objects.all().delete()
        # Also clean up categories to avoid orphans, duplicates or confusion
        Category.objects.all().delete()

        # Create Categories
        categories = ['Technology', 'Design', 'Artificial Intelligence', 'Productivity', 'Programming', 'Startup']
        cat_objects = {}
        for cat_name in categories:
            cat, created = Category.objects.get_or_create(name=cat_name)
            cat_objects[cat_name] = cat

        # Create Users
        users_data = [
            {'username': 'julia_code', 'first_name': 'Julia', 'last_name': 'Roberts', 'email': 'julia@example.com', 'bio': 'Full-stack developer and open source enthusiast.'},
            {'username': 'david_design', 'first_name': 'David', 'last_name': 'Chen', 'email': 'david@example.com', 'bio': 'Product Designer with 10 years of experience.'},
            {'username': 'sarah_ai', 'first_name': 'Sarah', 'last_name': 'Connor', 'email': 'sarah@example.com', 'bio': 'AI Researcher writing about the future of intelligence.'},
        ]
        user_objects = []
        for u_data in users_data:
            user, created = User.objects.get_or_create(username=u_data['username'], defaults={
                'email': u_data['email'],
                'first_name': u_data['first_name'],
                'last_name': u_data['last_name']
            })
            # Ensure names are updated if user exists
            if not created:
                user.first_name = u_data['first_name']
                user.last_name = u_data['last_name']
                user.save()

            if created:
                user.set_password('password123')
                user.save()
                user.profile.bio = u_data['bio']
                user.profile.reputation = random.randint(100, 1000)
                user.profile.save()
            user_objects.append(user)

        # Real Article Content (Long Form)
        articles_data = [
            {
                'title': 'The Future of UI Design: Beyond Screens',
                'category': 'Design',
                'author': 'david_design',
                'views': 12500,
                'content': """The way we interact with technology is changing. For decades, the screen has been our primary window into the digital world. But as we move toward 2030, user interface design is shifting from pixel-perfect screens to immersive, ambient experiences.

### The Rise of Voice and Gesture
Voice interfaces like Siri and Alexa were just the beginning. The next generation of UI will be completely hands-free and screen-free. Imagine controlling your home environment not by tapping a glass rectangle, but by simple, natural gestures in the air. We are already seeing the precursors to this with devices like the Apple Vision Pro and Meta Quest, where eye tracking and subtle finger pinches replace the mouse cursor.

### Ambient Computing
Technology is becoming invisible. It's no longer about a device you hold, but an environment you inhabit. Smart surfaces, haptic feedback integration in clothing, and augmented reality overlays will make "computing" feel like magic. 

> "Good design is obvious. Great design is transparent." — Joe Sparano

### The Role of AI in Generative UI
Artificial Intelligence is not just generating text and images; it's generating interfaces on the fly. Instead of a static dashboard that looks the same for everyone, imagine an interface that adapts to your current context, mood, and intent. If you're in a hurry, it shows big buttons and essential info. If you're exploring, it reveals depth and detail.

Designers must now think in 3D space, considering context, timing, and sensory feedback beyond just the visual. The challenge isn't making it look good; it's making it feel natural."""
            },
            {
                'title': 'Why Python Will Dominate the Next Decade',
                'category': 'Programming',
                'author': 'julia_code',
                'views': 8900,
                'content': """Python has been around for over 30 years, yet it feels younger and more vital than ever. Why does this language continue to eat the world? The answer lies in its versatility, its massive community, and its adaptability to new paradigms.

### 1. The AI and Data Science Explosion
Python is the lingua franca of Artificial Intelligence. Libraries like TensorFlow, PyTorch, and Scikit-learn have made it indispensable. You simply cannot do serious machine learning work without touching Python. Its syntax maps nealty to mathematical concepts, making it the preferred choice for researchers and data scientists.

### 2. Web Development Velocity
With frameworks like Django, FastAPI, and Flask, building robust backends is faster than ever. 
*   **Django**: The "batteries-included" framework for rapid development.
*   **FastAPI**: For high-performance APIs using modern Python type hints.
*   **Flask**: For microservices and simple apps.

### 3. Automation and DevOps
From simple scripts to complex DevOps pipelines, Python is the glue that holds infrastructure together. Ansible, SaltStack, and countless CI/CD tools rely on Python.

### The Simplicity Factor
Python's syntax is readable. It reads like English. This lowers the barrier to entry, allowing scientists, mathematicians, and artists to start coding without a computer science degree. As software eats the world, everyone needs to speak the language of software, and for most, that language is Python."""
            },
            {
                'title': 'Machine Learning: A Gentle Introduction',
                'category': 'Science',
                'author': 'sarah_ai',
                'views': 15600,
                'content': """Machine Learning (ML) sounds intimidating, but at its core, it's just about finding patterns in data. Instead of explicitly programming rules (if x then y), we feed the computer data and let it figure out the rules.

### How do machines "learn"?
Imagine teaching a child to recognize a dog. You don't explain that a dog has four legs, fur, and a bark (cats have those too!). Instead, you show them thousands of pictures of dogs and say "This is a dog." Eventually, they learn the pattern. Neural networks work broadly the same way.

### Supervised vs. Unsupervised Learning
*   **Supervised Learning**: Like a teacher with a student. We give the model data with the "correct" answers attached (labels). It learns to predict the answer for new data. This is used for spam filters, image recognition, and predictive analytics.
*   **Unsupervised Learning**: The student is left alone with a pile of books. The model looks for structure, clusters, or anomalies in unlabeled data. This is used for customer segmentation and recommendation engines.

### Real World Applications
We see ML everywhere today:
1.  **Recommendation systems**: Netflix knows what you want to watch before you do.
2.  **Fraud detection**: Banks analyze millions of transactions to spot weird patterns.
3.  **Medical diagnosis**: AI can spot tumors in X-rays with higher accuracy than some doctors.
4.  **Self-driving cars**: Processing visual data in real-time to navigate the world.

The revolution is just getting started, and it's going to reshape every industry."""
            },
            {
                'title': 'The Art of Minimalist Living',
                'category': 'Life',
                'author': 'sarah_ai',
                'views': 3200,
                'content': """Minimalism isn't just about having less stuff. It's about making room for more of what matters. In a world of constant distraction, clearing the clutter—both physical and mental—can be transformative.

### The Cost of Clutter
Every object you own extracts a tax. You have to clean it, store it, move it, and worry about it breaking. Physical clutter competes for your attention. By reducing what you own, you reclaim your energy.

### Start Small
You don't need to throw away everything you own. Start with one drawer. One shelf. Ask yourself: "Does this Spark Joy?" (Marie Kondo style) or simply "Is this useful?". If the answer is no, thank it for its service and let it go.

### Digital Minimalism
The clutter on our phones is often more damaging than the clutter in our closets.
*   **Unsubscribe**: Be ruthless with newsletters you delete without opening.
*   **Notifications**: Turn them off. All of them, except maybe phone calls.
*   **Home Screen**: Remove apps that trigger "doom scrolling".

Reclaim your attention. It's your most valuable resource."""
            },
            {
                'title': 'A Guide to Modern CSS Grid',
                'category': 'Programming',
                'author': 'julia_code',
                'views': 4500,
                'content': """CSS Grid Layout has revolutionized web design. It offers a grid-based layout system, with rows and columns, making it easier to design web pages without having to use floats and positioning.

### The Old Way vs The New Way
Remember `float: left`? Remember `clearfix` hacks? Remember inline-block spacing issues? Those days are gone. Flexbox solved 1D layouts, but Grid is here for the big picture.

### Why Grid?
*   **2-Dimensional**: Flexbox is 1D (row OR column), Grid is 2D (row AND column).
*   **Source Order Independence**: You can move items around the grid visually without changing the HTML structure. This is huge for accessibility and responsive design.
*   **Grid Template Areas**: You can literally draw your layout in ASCII art within your CSS.

```css
.container {
  display: grid;
  grid-template-areas: 
    "header header header"
    "sidebar main main"
    "footer footer footer";
}
```

It's time to stop fearing the grid and start building cleaner, more robust layouts."""
            },
            {
                'title': 'Exploring the Mountains of Patagonia',
                'category': 'Life',
                'author': 'david_design',
                'views': 1200,
                'content': """Last month, I unplugged from the digital world and spent two weeks hiking through Patagonia. The silence was deafening, and the views were humbling.

### Torres del Paine
The famous towers did not disappoint. Waking up at 4 AM to hike to the base for sunrise was grueling, but seeing the granite peaks glow red was worth every step. The wind in Patagonia is legendary—it can knock you off your feet—but it makes you feel alive.

### Disconnecting to Reconnect
We spend so much time looking at screens that we forget to look at the sky. There is no Wi-Fi in the wilderness, but I found a better connection.

> "Keep close to Nature's heart... and break clear away, once in a while, and climb a mountain or spend a week in the woods. Wash your spirit clean." — John Muir

Nature has a way of resetting our perspective. We worry about pixels and code, but the mountains have been here for millions of years, indifferent to our deadlines."""
            },
            {
                'title': 'The Science of Sleep',
                'category': 'Science',
                'author': 'sarah_ai',
                'views': 7800,
                'content': """We spend a third of our lives doing it, but we still don't fully understand it. Sleep is the single most effective way to reset our brain and body health each day.

### Why We Sleep
Matthew Walker, in his book "Why We Sleep", argues that sleep enriches a diversity of functions, including our ability to learn, memorize, and make logical decisions. It recalibrates our emotional brain circuits, allowing us to navigate next-day social and psychological challenges with cool-headed composure.

### The Sleep Crisis
Modern society is chronically sleep-deprived. Electric lighting, caffeine, and screens have waged war on our circadian rhythms.
*   **Memory**: Sleep is the "save button" for new memories.
*   **Health**: Short sleep predicts a shorter life span. It is linked to Alzheimer's, cancer, and heart disease.

### Tips for Better Sleep
1.  **Consistency**: Go to bed and wake up at the same time.
2.  **Darkness**: Melatonin needs darkness to work.
3.  **Temperature**: Keep your room cool (around 65°F / 18°C)."""
            },
            {
                'title': 'Rust vs Go: Which one to choose?',
                'category': 'Technology',
                'author': 'julia_code',
                'views': 15400,
                'content': """The debate rages on. Rust and Go are two of the most popular modern systems programming languages. But they solve different problems.

### Go: Simplicity and Concurrency
Go (Golang) was built by Google to solve scale. It's simple, fast to compile, and has amazing built-in concurrency (Goroutines). It's perfect for microservices and cloud infrastructure. You can learn Go in a weekend.

### Rust: Safety and Performance
Rust guarantees memory safety without a garbage collector. It forces you to write correct code. It's steeper to learn—the borrow checker is infamous—but once it compiles, it runs blazingly fast and won't crash from memory errors.

### The Verdict?
*   Building a **web server** or **microservice**? Go might be faster to ship.
*   Building a **browser engine**, **operating system**, or **game engine**? Rust is the clear winner.
*   Building CLI tools? Both are excellent.

Don't treat it as a war. Use the right tool for the job. Both languages are shaping the future of backend development."""
            }
        ]
        
        # Create 'Science' and 'Life' categories if they don't exist in the initial list
        extra_categories = ['Science', 'Life', 'Technology']
        for cat_name in extra_categories:
            cat, created = Category.objects.get_or_create(name=cat_name)
            cat_objects[cat_name] = cat

        for article_data in articles_data:
            # Get or Create Author
            author = User.objects.get(username=article_data['author'])
            category = cat_objects[article_data['category']]
            
            # Update or Create Article
            article, created = Article.objects.update_or_create(
                title=article_data['title'],
                defaults={
                    'author': author,
                    'category': category,
                    'content': article_data['content'],
                    'views': article_data['views'],
                    'is_published': True
                }
            )
            if created:
                self.stdout.write(f'Created article: {article.title}')
            else:
                self.stdout.write(f'Updated article: {article.title}')

        self.stdout.write(self.style.SUCCESS('Real data seeded successfully.'))
