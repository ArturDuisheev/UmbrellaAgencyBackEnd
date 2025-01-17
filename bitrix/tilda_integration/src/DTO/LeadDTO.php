<?php
namespace App\DTO;


use Symfony\Component\Validator\Constraints as Assert;
class LeadDTO
{
   /* #[Assert\NotBlank(message: 'Name is required.')]
    #[Assert\Type('string')]
    public string $name;

    #[Assert\NotBlank(message: 'Email is required.')]
    #[Assert\Email(message: 'Invalid email format.')]
    public string $email;

    #[Assert\NotBlank(message: 'Age is required.')]
    #[Assert\Type('integer')]
    #[Assert\GreaterThan(0, message: 'Age must be greater than 0.')]
    public int $age;*/
}
