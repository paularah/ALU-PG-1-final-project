from create_profiles import holder
from create_profiles import create_student_profile


def save_student_profile(holder):
    #a functionality to take student profile object and save them for reference
    profile = [holder.student_name]
    profile.append(holder.student_age)
    profile.append(holder.student_nationality)
    profile.append(holder.student_major)
    profile.append(holder.student_year)
    return profile



