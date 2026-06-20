## Challenge
![challenge-butterfly theory](./chaos%20theory%20(1).png)
### Python code
```python
temperature = float(input("Enter the temperature (ºC): "))
humidity = float(input("Enter the humidity (%): "))
wind_speed = float(input("Enter wind speed (km/h): "))

if humidity > 80:
      if temperature > 30:
            if wind_speed > 40:
                  print("Severe Storm Warning")
            else:
                  print("Heavy rain expected")
      else:
            print("Cloudy weather")
else:
      if temperature > 35:
            print("Heat wave alert")
      else:
            print("Normal weather")
```
### Butterfly Effect & Chaos Theory
- **Butterfly Effect**
	- the idea that small, seemingly insignificant actions can cause massive, unpredictable consequences downstream
	- foundational principle of Chaos Theory
- **Chaos Theory**
	- the branch of mathematics and physics that deals with systems that look completely random, unpredictable, and messy on the surface, but are actually governed by strict underlying laws
- If the Butterfly Effect is the concept (small changes cause big results), Chaos Theory is the entire field of study dedicated to figuring out how and why that happens