import math 
def footing_size_first_principles(load_kN: float, bearing_capacity_kPa: float, safety_factor: float = 1.5) -> None:
    """
    Calculates the minimum square footing size based on first principles.
    Formula: A = P / q_allow
    
    :param load_kN: Applied vertical load in kN
    :param bearing_capacity_kPa: Allowable soil bearing capacity in kPa
    :param safety_factor: Factor of safety to apply to bearing capacity (default = 1.5)
    """
    if bearing_capacity_kPa <= 0:
        raise ValueError("Bearing capacity must be greater than zero.")
    
    # Adjust allowable bearing capacity by safety factor
    q_safe = bearing_capacity_kPa / safety_factor
    
    # Compute required footing area (A = P / q)
    area_m2 = load_kN / q_safe
    
    # Assume square footing, so side length = sqrt(area)
    side_length_m = area_m2 ** 0.5
    
    # Print results
    print(f"Required footing area: {area_m2:.3f} m²")
    print(f"Approximate footing size: {side_length_m:.3f} m × {side_length_m:.3f} m")

# Example usage
#footing_size_first_principles(40, 100)
if __name__ == "__main__":
    footing_size_first_principles(40, 100)



def get_val_stress_point_load(p=None,z=None,r=None):
    """
    p is the point load reported in kN
    z depth of the point of calculation measured in meters
    r horizontal distance from the point of application to the examined point
    """
    sigma_z = 3*p*z**3 / (2*math.pi* (r**2+z**2)**(5/2))
    print(f'Calculated vertical stress at the depth {z:.2f} meters ,  horizontal distance {r:.2f}meters measured from the point of application is = {sigma_z}kN/m^2')

    return sigma_z
if __name__ == "__main__":
    get_val_stress_point_load(10,z=3,r=3)