from django.http import HttpResponse
import os
import sys
import time
import random
import math
import pprint


page_template = """
<div style="background-color: black; color: white; height: 80vh;">
<p style="font-size: 1.5rem; font-family: Papyrus;">
Our God is an awesome God
</p>
<p style="font-size: 1.5rem; font-family: Papyrus;">
He reigns
</p>
<p style="font-size: 1.5rem; font-family: Papyrus;">
From Heaven Above
</p>
<p style="font-size: 1.5rem; font-family: Papyrus;">
With Wisdom
</p>
<p style="font-size: 1.5rem; font-family: Papyrus;">
Power and Love
</p>
<p style="font-size: 1.5rem; font-family: Papyrus;">
Our God is an Awesome God
</p>
<button>Button</button>
</div>
"""
page_template2 = """
<div>
<h3>heading three</h3>
</div>
"""

def index(request):
    return HttpResponse("Hello, world")

def header(request):
    return HttpResponse([page_template, page_template2])