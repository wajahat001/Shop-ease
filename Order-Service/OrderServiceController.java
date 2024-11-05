package com.example.orderservice.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.Arrays;
import java.util.List;

@RestController
public class OrderServiceController {

    @GetMapping("/order-services")
    public String getOrderServices() {
        StringBuilder response = new StringBuilder();

        // Main heading
        response.append("<h1>Order Services</h1>");

        // Subheadings of related services
        List<String> services = Arrays.asList(
                "Order Management",
                "Payment Processing",
                "Order Tracking",
                "Order History",
                "Refund Management",
                "Inventory Check",
                "Shipping Services"
        );

        // Append subheadings
        for (String service : services) {
            response.append("<h2>").append(service).append("</h2>");
        }

        return response.toString();
    }
}
