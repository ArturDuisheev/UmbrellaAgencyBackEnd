<?php

namespace App\Controller;

use CrmMakeLeadService;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;

final class LeadController extends AbstractController
{
    public function __construct(private CrmMakeLeadService $crmMakeLeadService)
    {
    }

    #[Route("/", name: 'app_lead', methods: ['POST'])]
    public function index(): Response
    {
        return new Response('OK', Response::HTTP_OK);
    }
}
